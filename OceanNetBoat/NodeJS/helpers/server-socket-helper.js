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
            var seastateHelper = require('./seastate_helper');
            seastateHelper.retryPendingRecords();
            var performanceHelper = require('./performance_helper');
            performanceHelper.retryPendingRecords();
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
        socketHelper.socket.on('seastateBulkDataConf',function(ids){
            // logger.info("bulk_data_conf %s",JSON.stringify(ids));
            var seastateHelper = require('./seastate_helper');
            seastateHelper.bulkUpdate(ids);
        });
        socketHelper.socket.on('performanceBulkDataConf',function(ids){
            // logger.info("bulk_data_conf %s",JSON.stringify(ids));
            var performanceHelper = require('./performance_helper');
            performanceHelper.bulkUpdate(ids);
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
    },
    sendSeastateBulkData:function (pendingSeastateValues) {
        var payLoad = {};
        payLoad.userName = config.userName;
        payLoad.boatName = config.boatName;
        payLoad.boatSSID = require('./boat_data_helper').thisBoatSSID;
        payLoad.batchSize = pendingSeastateValues.length;
        payLoad.data = pendingSeastateValues;
        this.socket.emit('seastateBulkData',payLoad);
    },
    sendPerformanceBulkData:function (pendingPerformanceValues) {
        var payLoad = {};
        payLoad.userName = config.userName;
        payLoad.boatName = config.boatName;
        payLoad.boatSSID = require('./boat_data_helper').thisBoatSSID;
        payLoad.batchSize = pendingPerformanceValues.length;
        payLoad.data = pendingPerformanceValues;
        this.socket.emit('performanceBulkData',payLoad);
    }
};
var socketHelper = ServerSocketHelper;

module.exports = ServerSocketHelper;

