/**
 * Created by nkn on 2/27/2015.
 */
"use strict";

module.exports = function(sequelize, DataTypes) {
    var BoatData = sequelize.define("BoatData", {
            ID: {
                type: DataTypes.INTEGER,
                autoIncrement: true,
                primaryKey : true
            },
            ssid: {
                type: DataTypes.STRING,
                allowNull : false
            },
            CPE: {
                type: DataTypes.STRING,
                allowNull : false
            }
        },
        {
            tableName:'boat_data',
            timestamps:false
        });

    return BoatData;
};