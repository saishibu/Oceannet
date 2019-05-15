var loggerHelper = require('./helpers/logger_helper');
loggerHelper.init();
var models = require('./models');
var loggger = loggerHelper.logger;
models.sequelize.sync().then(function(){
    require('./helpers/boat_data_helper');
    require('./helpers/gps-data-helper');
    var gpsReceiver = require('./helpers/gps_receiver');
    gpsReceiver.init();
    var socketHelper = require('./helpers/server-socket-helper');
    socketHelper.init();
    setTimeout(function(){
        gpsReceiver.close();
        setTimeout(function(){
            loggger.info("***Closing the server after 10 mins")
            process.exit();
        },5000)
    },10*60*1000)
});
/*
var detectSSid = require('detect-ssid');
detectSSid(function(error, ssidname) {
    console.log("SSID:"+ssidname);
});*/