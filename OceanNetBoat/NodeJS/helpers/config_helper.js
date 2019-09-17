/**
 * Created by nkn on 2/25/2015.
 */
"use strict";
var config = require('../config/config.json');

var ConfigHelper = {
    envConfig:null,
    setConfig:function(){
        let envConfig = config[config.env];
        for(let key in envConfig){
            config[key] = envConfig[key];
        }
        this.envConfig = config;
    }
};
ConfigHelper.setConfig();
module.exports = ConfigHelper;
