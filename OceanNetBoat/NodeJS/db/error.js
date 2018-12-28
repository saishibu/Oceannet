/**
 * Created by sreedevi on 12-08-2015.
 */
var mysql = require('mysql');


var error = {
    handleConnectionError : function(err,myCon){
        if (err){
            var logger = require('../helpers/logger_helper').logger;
            myCon.end(function(err) {
                if(err)logger.error("Error while closing connection:"+err);
            });
            logger.error("Error while executing query:"+err);
            throw err;
        }
    }
}
module.exports = exports = error;