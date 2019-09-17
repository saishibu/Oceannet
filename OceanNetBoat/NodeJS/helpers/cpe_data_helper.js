/**
 * Created by nkn on 2/25/2015.
 */
"use strict";
var logger = require('./logger_helper').logger;
var models = require('../models');
var db = require('../db/db_connection_pool');
var error = require('../db/error');
var serverSocketHelper = require('./server-socket-helper');

var CPEDataHelper = {
    getLatest:function () {
        var helper = this;
        return models.CPEData.max('ID').then(function (max) {
            if(max > 0){
                return models.CPEData.findById(max);
            }
        });
    },
    cleanup:function(cpeId){
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
            var cleanupQuery = "delete from proto1 where ID < "+cpeId+";";
            // logger.info('cleanupQueryCPE:'+cleanupQuery);
            myCon.query(cleanupQuery
                , function(err, results) {
                    error.handleConnectionError(err,myCon);
                    // logger.info('Successfully cleaned up data');
                    myCon.release(function(err) {
                        if(err)logger.error("Error while closing connection:"+err);
                    });
                });
        })
    }
};
module.exports = CPEDataHelper;
