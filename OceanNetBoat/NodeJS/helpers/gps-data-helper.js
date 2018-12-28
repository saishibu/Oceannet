/**
 * Created by nkn on 2/25/2015.
 */
"use strict";
var logger = require('./logger_helper').logger;
var models = require('../models');
var db = require('../db/db_connection_pool');
var error = require('../db/error');
var serverSocketHelper = require('./server-socket-helper');

var GPSDataHelper = {
    limit:50,
    maxId:0,
    getMaxKey:function () {
        var helper = this;
        models.GPSData.max('gpsDataId').then(function (max) {
            if(max > 0){
                helper.maxId = max;
            }
        });
    },
    getNextMaxKey:function () {
        return ++this.maxId;
    },
    findById:function(id){
        return models.GPSData.findById(id);
    },
    findAllPendingForRetry:function(limit,offset){
        return models.GPSData.findAll({where:{transferDate:{$eq:null}},order:[['gpsDate','ASC']],offset: offset, limit: limit});
    },
    sendPendingRecords:function (offset,helper) {
        if(!serverSocketHelper.isConnected){
            return;
        }
        helper.findAllPendingForRetry(helper.limit,offset).then(function (pendingGPSDataValues) {
            if(pendingGPSDataValues.length > 0){
                logger.info("Number of pending records for retry %d",pendingGPSDataValues.length);
                var serverSocketHelper = require('./server-socket-helper');
                serverSocketHelper.sendBulkData(pendingGPSDataValues);
                if(pendingGPSDataValues.length < helper.limit){
                    // helper.retryPendingRecords(0,5*60*1000);
                }else{
                    offset += pendingGPSDataValues.length;
                    helper.retryPendingRecords(offset);
                }
            }/*else{
                helper.retryPendingRecords(0,5*60*1000);
            }*/
        });
    },
    retryPendingRecords:function (offset=0,timeout=3000) {
        // var envConfig = require('./config_helper').envConfig;
        // logger.info("Retrying pending records with Offset %s",offset);
        var helper = this;
        setTimeout(helper.sendPendingRecords,timeout,0,helper);
    },
    create:function(gpsData){
        return models.GPSData.create(gpsData);
    },
    bulkCreate:function(gpsDatas){
        models.GPSData.bulkCreate(gpsDatas);
    },
    update:function(gpsDataId){
        return this.findById(gpsDataId).then(function(gpsData){
            if(gpsData){
                gpsData.transferDate = new Date();
                return gpsData.save();
            }
        });
    },
    bulkUpdate:function (gpsDataIds) {
        db.pool.getConnection(function(err, myCon) {
            if (err) {
                logger.error("Error while acquiring connection:" + err);
                return;
            }
            if (!myCon) {
                logger.error("Error while acquiring connection:");
                return;
            }
            var updateQuery = "update GPSData ";
            updateQuery += "SET transferDate = NOW() "
            updateQuery += " Where gpsDataId in (";
            updateQuery += gpsDataIds.join(",");
            updateQuery += " )";
            // logger.info('updateQuery:'+updateQuery);
            myCon.query(updateQuery
                , function(err, results) {
                    error.handleConnectionError(err,myCon);
                    logger.info('Successfully updated data');
                    myCon.release(function(err) {
                        if(err)logger.error("Error while closing connection:"+err);
                    });
                });
        })
    },
    cleanup:function(){
        let helper = this;
        db.pool.getConnection(function(err, myCon) {
            if (err) {
                logger.error("Error while acquiring connection:" + err);
                return;
            }
            if (!myCon) {
                logger.error("Error while acquiring connection:");
                return;
            }
            let date = new Date();
            let hourStr = date.getDate()+"-"+(date.getMonth()+1)+"-"+date.getFullYear()+" "+(date.getHours()-1);
            var cleanupQuery = "delete from GPSData where transferDate is NOT NULL and gpsDate < str_to_date('"+hourStr+"','%d-%m-%Y %H');";
            logger.info('cleanupQuery:'+cleanupQuery);
            myCon.query(cleanupQuery
                , function(err, results) {
                    error.handleConnectionError(err,myCon);
                    logger.info('Successfully cleaned up data');
                    myCon.release(function(err) {
                        if(err)logger.error("Error while closing connection:"+err);
                    });
                    setTimeout(function(){
                        helper.cleanup();
                    },30*60*1000);
                });
        })
    }
};
GPSDataHelper.getMaxKey();
GPSDataHelper.cleanup();
module.exports = GPSDataHelper;
