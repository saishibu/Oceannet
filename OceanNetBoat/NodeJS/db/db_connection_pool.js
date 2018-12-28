/**
 * Created by sreedevi on 23-08-2015.
 */
var mysql = require('mysql');
var dbConfig = require('../helpers/config_helper');

var DataBase = {
     env:dbConfig.envConfig,
     pool:null,
     createPool:function(){
         this.pool = mysql.createPool({
             connectionLimit : this.env.connectionLimit,
             host: this.env.host,
             port: this.env.port,
             database: this.env.database,
             user: this.env.username,
             password: this.env.password
         })
     }
}
DataBase.createPool();
module.exports = exports = DataBase;