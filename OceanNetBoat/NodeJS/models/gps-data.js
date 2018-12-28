/**
 * Created by nkn on 2/27/2015.
 */
"use strict";

module.exports = function(sequelize, DataTypes) {
    var GPSData = sequelize.define("GPSData", {
            gpsDataId: {
                type: DataTypes.INTEGER,
                autoIncrement: true,
                primaryKey : true
            },
            longitude: {
                type: DataTypes.DOUBLE,
                allowNull : false
            },
            latitude: {
                type: DataTypes.DOUBLE,
                allowNull : false
            },
            speed: {
                type: DataTypes.FLOAT
            },
            gpsDate: {
                type: DataTypes.DATE,
                allowNull : false
            },
            transferDate: {
                type: DataTypes.DATE
            },
            ssId: {
                type: DataTypes.STRING
            },
            signal: {
                type: DataTypes.INTEGER
            },
            ccq: {
                type: DataTypes.INTEGER
            },
            noisef: {
                type: DataTypes.INTEGER
            },
            distance: {
                type: DataTypes.INTEGER
            },
            frequency: {
                type: DataTypes.STRING
            },
            channel: {
                type: DataTypes.INTEGER
            },
            txrate: {
                type: DataTypes.FLOAT
            },
            rxrate: {
                type: DataTypes.FLOAT
            },
            POS: {
                type: DataTypes.INTEGER
            },
            DIR: {
                type: DataTypes.STRING
            }
        },
        {
            tableName:'GPSData',
            timestamps:false
        });

    return GPSData;
};