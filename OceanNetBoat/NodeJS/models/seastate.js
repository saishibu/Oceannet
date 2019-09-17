/**
 * Created by nkn on 2/27/2015.
 */
"use strict";

module.exports = function(sequelize, DataTypes) {
    var seastate = sequelize.define("seastate", {
            id: {
                type: DataTypes.INTEGER,
                autoIncrement: true,
                primaryKey : true
            },
            timestamp: {
                type: 'TIMESTAMP',
                allowNull : false
            },
            Ax: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            Ay: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            Az: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            Gx: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            Gy: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            Gz: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            Mx: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            My: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            Mz: {
                type: DataTypes.FLOAT,
                allowNull : false
            },
            Dir: {
                type: DataTypes.STRING,
                allowNull : false
            },
            magAngle: {
                type: DataTypes.INTEGER,
                allowNull : false
            },
            transferDate: {
                type: DataTypes.DATE
            }
        },
        {
            tableName:'seastate',
            timestamps:false
        });

    return seastate;
};