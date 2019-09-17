
DROP TABLE IF EXISTS `GPSData`;

CREATE TABLE `GPSData` (
  `gpsDataId` BIGINT NOT NULL AUTO_INCREMENT,
  `longitude` DOUBLE NOT NULL,
  `latitude` DOUBLE NOT NULL,
  `speed` FLOAT NULL,
  `gpsDate` datetime NOT NULL,
  `transferDate` datetime NULL DEFAULT NULL,
  `ssId` varchar(50) NULL,
  `signal` INT NULL,
  `ccq` FLOAT NULL,
  `noisef` INT NULL,
  `distance` INT NULL,
  `frequency` varchar(20) DEFAULT NULL,
  `channel` smallint DEFAULT NULL,
  `txrate` float DEFAULT NULL,
  `rxrate` float DEFAULT NULL,
	`POS` INT(11) NOT NULL,
	`DIR` TEXT NOT NULL,
  `bsip` varchar(50) NULL,
  `ping` INT NULL
  PRIMARY KEY (`gpsDataId`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

ALTER TABLE proto1 
ADD COLUMN `frequency` varchar(20) DEFAULT NULL,
ADD COLUMN `channel` smallint DEFAULT NULL,
ADD COLUMN `txrate` float DEFAULT NULL,
ADD COLUMN `rxrate` float DEFAULT NULL;

ALTER TABLE proto1 
ADD COLUMN `POS` int(11) NOT NULL,
ADD COLUMN `DIR` text NOT NULL;

ALTER TABLE GPSData 
ADD COLUMN `POS` int(11) NOT NULL,
ADD COLUMN `DIR` text NOT NULL;

ALTER TABLE GPSData 
ADD COLUMN `bsip` varchar(50) NULL,
ADD COLUMN `ping` INT NULL;

ALTER TABLE performance
ADD COLUMN `transferDate` datetime NULL DEFAULT NULL;
  
ALTER TABLE seastate
ADD COLUMN `transferDate` datetime NULL DEFAULT NULL;
    
