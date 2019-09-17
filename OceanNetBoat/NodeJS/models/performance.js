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
                type: 'TIMESTAMP',
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