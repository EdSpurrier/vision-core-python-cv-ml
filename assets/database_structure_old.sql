-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 20, 2019 at 05:17 PM
-- Server version: 5.6.41-84.1
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `edspurri_loggy`
--

-- --------------------------------------------------------

--
-- Table structure for table `grabs`
--

CREATE TABLE `grabs` (
  `grab_unique_id` int(11) NOT NULL,
  `timestamp` int(11) NOT NULL,
  `wood_type` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `actual_length` float DEFAULT NULL,
  `invoice_length` float DEFAULT NULL,
  `grab_img_url` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `location_type` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_unique_id` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

CREATE TABLE `logs` (
  `log_unique_id` int(11) NOT NULL,
  `log_id` int(11) NOT NULL,
  `log_img_url` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `barcode_img_url` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `grab_unique_id` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `grab_position_x` int(11) NOT NULL,
  `grab_position_y` int(11) NOT NULL,
  `grab_width` int(11) NOT NULL,
  `grab_height` int(11) NOT NULL,
  `actual_diameter` float NOT NULL,
  `jas_diameter` int(11) NOT NULL,
  `jas_cbm` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `grabs`
--
ALTER TABLE `grabs`
  ADD UNIQUE KEY `Grab Unique Id` (`grab_unique_id`);

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD UNIQUE KEY `Log Unique Id` (`log_unique_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `grabs`
--
ALTER TABLE `grabs`
  MODIFY `grab_unique_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `log_unique_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
