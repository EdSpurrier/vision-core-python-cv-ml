-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 03, 2019 at 03:03 AM
-- Server version: 5.7.24
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `loggy`
--

-- --------------------------------------------------------

--
-- Table structure for table `containers`
--

DROP TABLE IF EXISTS `containers`;
CREATE TABLE IF NOT EXISTS `containers` (
  `container_unique_id` int(11) NOT NULL AUTO_INCREMENT,
  `container_id` varchar(25) NOT NULL,
  `order_unique_id` int(11) NOT NULL,
  PRIMARY KEY (`container_unique_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `grabs`
--

DROP TABLE IF EXISTS `grabs`;
CREATE TABLE IF NOT EXISTS `grabs` (
  `grab_unique_id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` int(11) NOT NULL,
  `weight` int(10) DEFAULT NULL,
  `wood_type` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `actual_length` float DEFAULT NULL,
  `invoice_length` float DEFAULT NULL,
  `grab_img_url` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `location_type` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `container_unique_id` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  UNIQUE KEY `Grab Unique Id` (`grab_unique_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

DROP TABLE IF EXISTS `logs`;
CREATE TABLE IF NOT EXISTS `logs` (
  `log_unique_id` int(11) NOT NULL AUTO_INCREMENT,
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
  `jas_cbm` float DEFAULT NULL,
  UNIQUE KEY `Log Unique Id` (`log_unique_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `order_unique_id` int(20) NOT NULL AUTO_INCREMENT,
  `order_number` varchar(20) NOT NULL,
  `customer_name` varchar(30) NOT NULL,
  PRIMARY KEY (`order_unique_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
