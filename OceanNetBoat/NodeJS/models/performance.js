/**
 * Created by nkn on 2/27/2015.
 */
"use strict";

module.exports = function(sequelize, DataTypes) {
    var performance = sequelize.define("performance", {
            id: {
                type: DataTypes.INTEGER,
                autoIncrement: true,
                primaryKey : true
            },
            timestamp: {
                type: DataTypes.INTEGER,
                allowNull : false
            },
            temp: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            RAM: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            CPU: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            disk: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            CPUFreqCurrent: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            CPUFreqMin: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            CPUFreqMax: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            loadAvg1: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            loadAvg5: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            loadAvg15: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            bytes_sent: {
                type: DataTypes.INTEGER,
                allowNull : false
            },
            bytes_recv: {
                type: DataTypes.INTEGER,
                allowNull : false
            },
            packets_sent: {
                type: DataTypes.INTEGER,
                allowNull : false
            },
            packets_recv: {
                type: DataTypes.INTEGER,
                allowNull : false
            },
            errin: {
                type: DataTypes.INTEGER,
                allowNull : false
            },
            errout: {
                type: DataTypes.INTEGER,
                allowNull : false
            },
            dropin: {
                type: DataTypes.INTEGER,
                allowNull : false
            },
            dropout: {
                type: DataTypes.INTEGER,
                allowNull : false
            },
            transferDate: {
                type: DataTypes.DATE
            },
        },
        {
            tableName:'performance',
            timestamps:false
        });

    return performance;
};