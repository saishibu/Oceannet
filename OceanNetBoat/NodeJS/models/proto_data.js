/**
 * Created by nkn on 2/27/2015.
 */
"use strict";

module.exports = function(sequelize, DataTypes) {
    var CPEData = sequelize.define("CPEData", {
            ID: {
                type: DataTypes.INTEGER,
                autoIncrement: true,
                primaryKey : true
            },
            BOAT: {
                type: DataTypes.INTEGER
            },
            SS: {
                type: DataTypes.INTEGER
            },
            NF: {
                type: DataTypes.INTEGER
            },
            CCQ: {
                type: DataTypes.INTEGER
            },
            D: {
                type: DataTypes.INTEGER
            },
            RSSI: {
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
            tableName:'proto1',
            timestamps:false
        });

    return CPEData;
};