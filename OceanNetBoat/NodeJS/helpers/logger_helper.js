var winston = require('winston');
require('winston-daily-rotate-file');
const { combine, timestamp, label, printf,splat } = winston.format;

var LoggerHelper = {
    logger:null,
    init:function(){
        const myFormat = printf(info => {
            return `${new Date().toLocaleString()} ${info.level}: ${info.message}`;
          });
        var transport = new (winston.transports.DailyRotateFile)({
            filename: 'boat-%DATE%.log',
            datePattern: 'YYYY-MM-DD',
            zippedArchive: true,
            maxFiles: '5d'
          });
        this.logger = winston.createLogger({
            level: 'info',
            format: combine(
                timestamp(),
                splat(),
                myFormat
            )
        });
        this.logger.add(transport);
    }
};
module.exports = LoggerHelper;