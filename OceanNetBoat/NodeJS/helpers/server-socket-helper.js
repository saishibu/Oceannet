/**
 * Created by sreedevi on 13-04-2015.
 */
"use strict";

var logger = require('./logger_helper').logger;
var configHelper = require('./config_helper');
var config    = configHelper.envConfig;
const zlib = require('zlib');

var ServerSocketHelper = {
    serverTime:null,
    socket:null,
    isConnected:false,
    init:function(){
        this.socket = require('socket.io-client')(config.server);
        var socketHelper = this;
        socketHelper.socket.on('connect',function(){
            socketHelper.isConnected = true;
            var gpsDataHelper = require('./gps-data-helper');
            gpsDataHelper.retryPendingRecords();
        });
        socketHelper.socket.on('disconnect',function(){
            socketHelper.isConnected = false;
            logger.info("Disconnected for the socket id %s",socketHelper.socket.id);
        });
        socketHelper.socket.on('reconnect',function(){
            socketHelper.isConnected = true;
            logger.info("Reconnected for the socket id %s",socketHelper.socket.id);
        });
        socketHelper.socket.on('serverTime',function(serverTime){
            socketHelper.serverTime = serverTime;
        });
        socketHelper.socket.on('autosysDataConf',function(gpsDataId){
            var gpsDataHelper = require('./gps-data-helper');
            gpsDataHelper.update(gpsDataId);
        });
        socketHelper.socket.on('autosysBulkDataConf',function(gpsDataIds){
            // logger.info("bulk_data_conf %s",JSON.stringify(gpsDataIds));
            var gpsDataHelper = require('./gps-data-helper');
            gpsDataHelper.bulkUpdate(gpsDataIds);
        });
    },
    sendData:function (data) {
        let payLoad = {};
        payLoad.userName = config.userName;
        payLoad.boatName = config.boatName;
        payLoad.data = data;
        this.socket.emit('autosysData',payLoad);
    },
    sendBulkData:function (pendingGPSDataValues) {
        var payLoad = {};
        payLoad.userName = config.userName;
        payLoad.boatName = config.boatName;
        payLoad.batchSize = pendingGPSDataValues.length;
        payLoad.data = pendingGPSDataValues;
        this.socket.emit('autosysBulkData',payLoad);
    }
};
var socketHelper = ServerSocketHelper;

module.exports = ServerSocketHelper;

