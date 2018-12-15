-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 29, 2018 at 11:19 AM
-- Server version: 10.1.23-MariaDB-9+deb9u1
-- PHP Version: 7.0.27-0+deb9u1

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
  `ssid` text NOT NULL,
  `CPE` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `boat_data`
--

INSERT INTO `boat_data` (`ID`, `ssid`, `CPE`) VALUES
(1, 'sudhavarsham', '192.168.179.69'),
(2, 'amrithadev', '192.168.179.81'),
(3, 'amritakrishna', '192.168.179.73'),
(4, 'vedhika', '192.168.179.67'),
(5, 'aparna', '192.168.179.76'),
(6, 'amit', '192.179.168.107'),
(7, 'sarveshwarah', '192.179.168.116'),
(8, 'Oceannet_Test', '192.168.179.118');

-- --------------------------------------------------------

--
-- Table structure for table `gps_log`
--

CREATE TABLE `gps_log` (
  `ID` int(11) NOT NULL,
  `TIMESTAMP` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `BOAT` text NOT NULL,
  `LAT` text NOT NULL,
  `LON` text NOT NULL,
  `Speed` float NOT NULL,
  `temp` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gps_log`
--

INSERT INTO `gps_log` (`ID`, `TIMESTAMP`, `BOAT`, `LAT`, `LON`, `Speed`, `temp`) VALUES
(1, '2018-05-23 17:52:12', 'Grid_23_May_18', '0', '0', 0, 0),
(2, '2018-05-23 18:24:59', 'Grid_23_May_18', '0', '0', 0, 0),
(3, '2018-05-23 18:25:57', 'Grid_23_May_18', '0', '0', 0, 0),
(4, '2018-05-23 18:30:38', 'Grid_24_May_18', '0', '0', 0, 0),
(5, '2018-05-26 12:59:38', 'Grid_26_May_18', '0', '0', 0, 0),
(6, '2018-05-26 17:48:03', 'amit_26_May_18', '0', '0', 0, 0),
(7, '2018-05-26 17:49:03', 'amit_26_May_18', '0', '0', 0, 0),
(8, '2018-05-26 17:50:03', 'amit_26_May_18', '0', '0', 0, 0),
(9, '2018-06-25 10:10:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(10, '2018-06-25 10:15:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(11, '2018-06-25 10:20:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(12, '2018-06-25 10:25:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(13, '2018-06-25 10:30:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(14, '2018-06-25 10:35:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(15, '2018-06-25 10:40:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(16, '2018-06-25 10:45:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(17, '2018-06-25 10:50:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(18, '2018-06-25 10:55:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(19, '2018-06-25 11:00:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(20, '2018-06-25 11:05:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(21, '2018-06-25 11:10:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(22, '2018-06-25 11:15:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(23, '2018-06-25 11:20:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(24, '2018-06-25 11:25:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(25, '2018-06-25 11:30:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(26, '2018-06-25 11:35:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(27, '2018-06-25 11:40:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(28, '2018-06-25 11:45:03', 'amit_25_Jun_18', '0', '0', 0, 0),
(29, '1980-01-05 23:50:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(30, '2018-06-26 04:40:03', 'amit_26_Jun_18', '0', '0', 0, 0),
(31, '2018-06-26 04:45:03', 'amit_26_Jun_18', '0', '0', 0, 0),
(32, '2018-06-26 04:50:03', 'amit_26_Jun_18', '0', '0', 0, 0),
(33, '1980-01-05 23:50:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(34, '1980-01-05 23:55:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(35, '1980-01-06 00:00:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(36, '1980-01-06 00:05:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(37, '1980-01-06 00:10:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(38, '1980-01-06 00:15:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(39, '1980-01-06 00:20:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(40, '1980-01-06 00:25:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(41, '1980-01-06 00:30:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(42, '1980-01-06 00:35:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(43, '1980-01-06 00:40:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(44, '1980-01-06 00:45:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(45, '1980-01-06 00:50:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(46, '1980-01-06 00:55:04', 'amit_06_Jan_80', '0', '0', 0, 0),
(47, '1980-01-06 01:00:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(48, '1980-01-06 01:05:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(49, '1980-01-06 01:10:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(50, '1980-01-06 01:15:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(51, '1980-01-06 01:20:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(52, '1980-01-06 01:25:04', 'amit_06_Jan_80', '0', '0', 0, 0),
(53, '1980-01-06 01:30:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(54, '1980-01-06 01:35:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(55, '1980-01-05 23:50:03', 'amit_06_Jan_80', '0', '0', 0, 0),
(56, '1980-01-06 00:00:05', 'amit_06_Jan_80', '0', '0', 0, 0),
(57, '1980-01-06 01:05:05', 'amit_06_Jan_80', '0', '0', 0, 0),
(58, '1980-01-06 01:25:04', 'amit_06_Jan_80', '0', '0', 0, 0),
(59, '1980-01-06 01:45:04', 'amit_06_Jan_80', '0', '0', 0, 0),
(60, '1980-01-05 23:55:05', 'amit_06_Jan_80', '0', '0', 0, 0),
(61, '1980-01-06 00:00:05', 'jio_06_Jan_80', '0', '0', 0, 0),
(62, '1980-01-06 00:08:24', 'jio_06_Jan_80', '0', '0', 0, 0),
(63, '1980-01-06 00:08:29', 'jio_06_Jan_80', '0', '0', 0, 0),
(64, '1980-01-06 00:10:02', 'jio_06_Jan_80', '0', '0', 0, 0),
(65, '1980-01-06 00:25:55', 'jio_06_Jan_80', '0', '0', 0, 1),
(66, '1980-01-06 00:26:08', 'jio_06_Jan_80', '0', '0', 0, 1),
(67, '2018-06-29 05:40:26', 'jio_29_Jun_18', '0', '0', 0, 0),
(68, '2018-06-29 05:43:29', 'jio_29_Jun_18', '0', '0', 0, 37.9),
(69, '2018-06-29 05:44:27', 'jio_29_Jun_18', '0', '0', 0, 38.5),
(70, '2018-06-29 05:45:03', 'jio_29_Jun_18', '0', '0', 0, 39);

-- --------------------------------------------------------

--
-- Table structure for table `proto1`
--

CREATE TABLE `proto1` (
  `ID` int(11) NOT NULL,
  `TIMESTAMP` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `BOAT` text NOT NULL,
  `SS` int(11) NOT NULL,
  `NF` int(11) NOT NULL,
  `CCQ` int(11) NOT NULL,
  `D` int(11) NOT NULL,
  `RSSI` int(11) NOT NULL,
  `POS` int(11) NOT NULL,
  `DIR` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `proto1`
--

INSERT INTO `proto1` (`ID`, `TIMESTAMP`, `BOAT`, `SS`, `NF`, `CCQ`, `D`, `RSSI`, `POS`, `DIR`) VALUES
(1, '2018-05-23 16:19:54', 'dummy', 0, 0, 0, 0, 0, 0, '0'),
(2, '2018-05-23 17:49:32', 'test_setup_23_May_18', -41, -92, 966, 450, 55, 0, ''),
(3, '2018-05-23 17:49:37', 'test_setup_23_May_18', -40, -91, 957, 450, 56, 0, ''),
(4, '2018-05-23 17:49:43', 'test_setup_23_May_18', -40, -91, 959, 450, 56, 0, ''),
(5, '2018-05-23 17:49:48', 'test_setup_23_May_18', -47, -91, 939, 450, 49, 0, ''),
(6, '2018-05-23 17:49:53', 'test_setup_23_May_18', -51, -91, 926, 450, 45, 1, 'fwd'),
(7, '2018-05-23 17:49:59', 'test_setup_23_May_18', -50, -91, 919, 450, 46, 1, 'fwd'),
(8, '2018-05-23 17:50:04', 'test_setup_23_May_18', -48, -91, 863, 450, 48, 1, 'fwd'),
(9, '2018-05-23 17:50:09', 'test_setup_23_May_18', -50, -91, 838, 450, 46, 1, 'fwd'),
(10, '2018-05-23 17:50:15', 'test_setup_23_May_18', -51, -91, 846, 450, 45, 2, 'fwd'),
(11, '2018-05-23 17:50:20', 'test_setup_23_May_18', -54, -91, 894, 450, 42, 3, 'fwd'),
(12, '2018-05-23 17:50:26', 'test_setup_23_May_18', -54, -91, 829, 450, 42, 4, 'fwd'),
(13, '2018-05-23 17:50:31', 'test_setup_23_May_18', -57, -92, 777, 450, 39, 5, 'fwd'),
(14, '2018-05-23 17:50:36', 'test_setup_23_May_18', -51, -96, 810, 450, 45, 6, 'fwd'),
(15, '2018-05-23 17:50:42', 'test_setup_23_May_18', -51, -96, 856, 450, 45, 7, 'fwd');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `boat_data`
--
ALTER TABLE `boat_data`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `gps_log`
--
ALTER TABLE `gps_log`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `proto1`
--
ALTER TABLE `proto1`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `boat_data`
--
ALTER TABLE `boat_data`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `gps_log`
--
ALTER TABLE `gps_log`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;
--
-- AUTO_INCREMENT for table `proto1`
--
ALTER TABLE `proto1`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
