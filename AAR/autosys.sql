-- phpMyAdmin SQL Dump
-- version 4.6.6deb4+deb9u2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 18, 2021 at 07:12 AM
-- Server version: 10.1.48-MariaDB-0+deb9u1
-- PHP Version: 7.0.33-0+deb9u10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `autosys`
--

-- --------------------------------------------------------

--
-- Table structure for table `boat_data`
--

CREATE TABLE `boat_data` (
  `ID` int(11) NOT NULL,
  `CPE` text NOT NULL,
  `ssid` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `boat_data`
--

INSERT INTO `boat_data` (`ID`, `CPE`, `ssid`) VALUES
(1, '192.168.1.21', 'amit');

-- --------------------------------------------------------

--
-- Table structure for table `config`
--

CREATE TABLE `config` (
  `ip` varchar(20) NOT NULL,
  `log` tinyint(1) DEFAULT NULL,
  `piggyback` tinyint(1) DEFAULT NULL,
  `configtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `config`
--

INSERT INTO `config` (`ip`, `log`, `piggyback`, `configtime`) VALUES
('192.168.0.21', 1, 0, '2021-02-16 09:55:27'),
('192.168.1.21', 0, 0, '2021-02-16 11:04:06');

-- --------------------------------------------------------

--
-- Table structure for table `GPSData`
--

CREATE TABLE `GPSData` (
  `gpsDataId` bigint(20) NOT NULL,
  `longitude` double NOT NULL,
  `latitude` double NOT NULL,
  `speed` float DEFAULT NULL,
  `gpsDate` datetime NOT NULL,
  `transferDate` datetime DEFAULT NULL,
  `ssId` varchar(50) DEFAULT NULL,
  `signal` int(11) DEFAULT NULL,
  `ccq` float DEFAULT NULL,
  `noisef` int(11) DEFAULT NULL,
  `distance` int(11) DEFAULT NULL,
  `frequency` varchar(20) DEFAULT NULL,
  `channel` smallint(6) DEFAULT NULL,
  `txrate` float DEFAULT NULL,
  `rxrate` float DEFAULT NULL,
  `POS` int(11) NOT NULL,
  `DIR` text NOT NULL,
  `bsip` varchar(50) DEFAULT NULL,
  `ping` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `gps_log`
--

CREATE TABLE `gps_log` (
  `ID` int(11) NOT NULL,
  `TIMESTAMP` int(11) NOT NULL,
  `BOAT` int(11) DEFAULT NULL,
  `LAT` double NOT NULL,
  `LON` double NOT NULL,
  `Speed` float NOT NULL,
  `temp` float NOT NULL,
  `transfer_time` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `performance`
--

CREATE TABLE `performance` (
  `id` int(11) NOT NULL,
  `timestamp` int(11) NOT NULL,
  `temp` float NOT NULL,
  `RAM` float NOT NULL,
  `CPU` float NOT NULL,
  `disk` float NOT NULL,
  `CPUFreqCurrent` float NOT NULL,
  `CPUFreqMin` float NOT NULL,
  `CPUFreqMax` float NOT NULL,
  `loadAvg1` float NOT NULL,
  `loadAvg5` float NOT NULL,
  `loadAvg15` float NOT NULL,
  `bytes_sent` int(11) NOT NULL,
  `bytes_recv` int(11) NOT NULL,
  `packets_sent` int(11) NOT NULL,
  `packets_recv` int(11) NOT NULL,
  `errin` int(11) NOT NULL,
  `errout` int(11) NOT NULL,
  `dropin` int(11) NOT NULL,
  `dropout` int(11) NOT NULL,
  `transferDate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `performance`
--

INSERT INTO `performance` (`id`, `timestamp`, `temp`, `RAM`, `CPU`, `disk`, `CPUFreqCurrent`, `CPUFreqMin`, `CPUFreqMax`, `loadAvg1`, `loadAvg5`, `loadAvg15`, `bytes_sent`, `bytes_recv`, `packets_sent`, `packets_recv`, `errin`, `errout`, `dropin`, `dropout`, `transferDate`) VALUES
(1, 1569535487, 60.5, 81, 100, 9, 1000, 1000, 700, 0.34, 0.42, 0.44, 14913848, 10920236, 17578, 16573, 0, 0, 0, 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `proto1`
--

CREATE TABLE `proto1` (
  `ID` int(11) NOT NULL,
  `gps_ID` int(11) DEFAULT NULL,
  `TIMESTAMP` int(11) NOT NULL,
  `BOAT` int(11) NOT NULL,
  `SS` int(11) NOT NULL,
  `NF` int(11) NOT NULL,
  `CCQ` int(11) NOT NULL,
  `D` int(11) NOT NULL,
  `RSSI` int(11) NOT NULL,
  `POS` int(11) NOT NULL,
  `DIR` text NOT NULL,
  `frequency` varchar(20) DEFAULT NULL,
  `channel` smallint(6) DEFAULT NULL,
  `txrate` float DEFAULT NULL,
  `rxrate` float DEFAULT NULL,
  `bsip` text,
  `ping` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `configTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `configTime`, `username`, `password`) VALUES
(1, '2021-02-17 08:49:28', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `seastate`
--

CREATE TABLE `seastate` (
  `id` int(11) NOT NULL,
  `timestamp` int(11) NOT NULL,
  `Ax` float NOT NULL,
  `Ay` float NOT NULL,
  `Az` float NOT NULL,
  `Gx` float NOT NULL,
  `Gy` float NOT NULL,
  `Gz` float NOT NULL,
  `Mx` float NOT NULL,
  `My` float NOT NULL,
  `Mz` float NOT NULL,
  `Dir` varchar(20) NOT NULL,
  `magAngle` int(11) NOT NULL,
  `transferDate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `boat_data`
--
ALTER TABLE `boat_data`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID` (`ID`);

--
-- Indexes for table `config`
--
ALTER TABLE `config`
  ADD UNIQUE KEY `ip` (`ip`);

--
-- Indexes for table `GPSData`
--
ALTER TABLE `GPSData`
  ADD PRIMARY KEY (`gpsDataId`);

--
-- Indexes for table `gps_log`
--
ALTER TABLE `gps_log`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID` (`ID`),
  ADD KEY `BOAT` (`BOAT`);

--
-- Indexes for table `performance`
--
ALTER TABLE `performance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `proto1`
--
ALTER TABLE `proto1`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `gps_ID` (`gps_ID`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `seastate`
--
ALTER TABLE `seastate`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `boat_data`
--
ALTER TABLE `boat_data`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `GPSData`
--
ALTER TABLE `GPSData`
  MODIFY `gpsDataId` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `gps_log`
--
ALTER TABLE `gps_log`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `performance`
--
ALTER TABLE `performance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `proto1`
--
ALTER TABLE `proto1`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=148769;
--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `seastate`
--
ALTER TABLE `seastate`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6533312;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
