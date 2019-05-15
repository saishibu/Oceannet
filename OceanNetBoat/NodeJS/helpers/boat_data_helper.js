/**
 * Created by nkn on 2/25/2015.
 */
"use strict";
var models = require('../models');
var logger = require('./logger_helper').logger;

var BoatDataHelper = {
    cacheLoaded:false,
    updateCache:function(){
        logger.info("BoatData helper: Cache start");
        var boatDataHelper = this;
        var promise = this.findAllCache();
        promise.then(function(boatDatas){
            boatDatas.forEach(function(boatData){
                boatDataHelper.addToCache(boatData);
            });
            logger.info("boatDataHelper.cacheLoaded = true");
            boatDataHelper.cacheLoaded = true;
        });
    },
    addToCache:function(boatData){
        if(!this.boatDatas){
            this.boatDatas = [];
        }
        this.boatDatas.push(boatData);
        this[boatData.ID] = boatData;
    },
    findAllCache:function(){
       return models.BoatData.findAll();
    }
};

BoatDataHelper.updateCache();

module.exports = BoatDataHelper;
