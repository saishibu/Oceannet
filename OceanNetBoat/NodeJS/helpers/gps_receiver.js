/**
 * Created by sreedevi on 20-11-2015.
 */
var logger = require('./logger_helper').logger;
var configHelper    = require('./config_helper');
var gpsDataHelper = require('./gps-data-helper');
const nmea = require('node-nmea');
var socketHelper = require('./server-socket-helper');
var cpeDataHelper = require('./cpe_data_helper');
var boatDataHelper = require('./boat_data_helper');

var GPSReceiver = {
    serialPort:null,
    parser:null,
    gpsGGA:null,
    gpsRMC:null,
    init:function () {
        var receiver = this;
        var config = configHelper.envConfig;
        logger.info("Config:"+JSON.stringify(config));
        const SerialPort = require('serialport')
        const Readline = require('@serialport/parser-readline')
        this.serialPort = new SerialPort(config.serialPortName,{baudRate: config.baudRate});
        this.parser = this.serialPort.pipe(new Readline({ delimiter: '\r\n' }))
        logger.info("serialPort is not open yet");
        this.serialPort.on ('open', function (error) {
            if(error){
                logger.error("Failed to open the serial port %s with error %s",config.serialPortName,error);
                return;
            }else{
                logger.info(config.serialPortName+" : is open");
                receiver.parser.on ('data',function(line){
                    // logger.info("data from:"+config.serialPortName+":" + line);
                    if(line.indexOf('$GPGGA') === 0){
                        receiver.gpsGGA = line;
                        // logger.info("Parsed data No Time:"+JSON.stringify(nmeaData))
                    }else if(line.indexOf('$GPRMC') === 0){
                        receiver.gpsRMC = line;
                        // logger.info("Parsed data No Time:"+JSON.stringify(nmeaData))
                    }
                });
            }
        });
        this.serialPort.on ('close', function (error) {
            if(error){
                logger.info("error while closing serialPort:"+config.serialPortName+":" + error);
            }else{
                logger.info("Closed serialPort:"+config.serialPortName+": Successfully");
            }
        });
        this.serialPort.on ('error', function (error) {
            if(error){
                logger.info("error occurred with serialPort:"+config.serialPortName+":" + error);
            }
        });
        setInterval(function(){
            // logger.info("Set Interval")
            receiver.processData();
        },60000)
    },
    close:function(){
        this.serialPort.close();
        logger.info("***Close started for serial port");
    },
    processData:async function(){
        // logger.info("processData")
        if(this.gpsGGA || this.gpsRMC){
            let rawData = null;
            if(this.gpsRMC){
                rawData = nmea.parse(this.gpsRMC);
                // logger.info("Parsed gpsRMC:"+JSON.stringify(this.gpsRMC))
            }else if(this.gpsGGA){
                rawData = nmea.parse(this.gpsGGA);
                // logger.info("Parsed gpsGGA:"+JSON.stringify(this.gpsGGA))
            }
            if(rawData.valid){
                let gpsData = {};
                gpsData.longitude = rawData.loc.geojson.coordinates[0];
                gpsData.latitude = rawData.loc.geojson.coordinates[1];
                gpsData.gpsDate = new Date(rawData.datetime);
                gpsData.speed = (rawData.speed*1000)/3600;
                if(!gpsData.speed){
                    gpsData.speed = 0;
                }
                gpsData.gpsDataId = gpsDataHelper.getNextMaxKey();
                let cpeData = await cpeDataHelper.getLatest();
                if(cpeData){
                    let boatData = boatDataHelper[cpeData.BOAT];
                    if(boatData){
                        gpsData.ssId = boatData.ssid;
                    }
                    gpsData.signal = cpeData.SS;
                    gpsData.noisef = cpeData.NF;
                    gpsData.ccq = cpeData.CCQ;
                    gpsData.distance = cpeData.D;
                    gpsData.frequency = cpeData.frequency;
                    gpsData.channel = cpeData.channel;
                    gpsData.txrate = cpeData.txrate;
                    gpsData.rxrate = cpeData.rxrate;
                    gpsData.POS = cpeData.POS;
                    gpsData.DIR = cpeData.DIR;
                    gpsData.bsip = cpeData.bsip;
                    gpsData.ping = cpeData.ping;
                }
                await gpsDataHelper.create(gpsData);
                socketHelper.sendData(gpsData);
                if(cpeData){
                    cpeDataHelper.cleanup(cpeData.ID);
                }
            }
            // logger.info("gpsData:"+JSON.stringify(gpsData))
            this.gpsGGA = null;
            this.gpsRMC = null;
        }
    }
};
module.exports = exports = GPSReceiver;