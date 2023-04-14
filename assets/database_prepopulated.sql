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
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `containers`
--

INSERT INTO `containers` (`container_unique_id`, `container_id`, `order_unique_id`) VALUES
(1, 'CHUY20918273', 1),
(2, 'CBBA25411847', 1),
(3, 'ABCD33918273', 2),
(4, 'PPOQ25661889', 1),
(5, 'CAAC36218121', 2);

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
) ENGINE=MyISAM AUTO_INCREMENT=1554168117 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `grabs`
--

INSERT INTO `grabs` (`grab_unique_id`, `timestamp`, `weight`, `wood_type`, `actual_length`, `invoice_length`, `grab_img_url`, `location_type`, `container_unique_id`) VALUES
(1554168116, 1554168116, NULL, NULL, NULL, NULL, 'http://lumigear.net/loggy/grabs/1554168116.jpg', NULL, NULL),
(1554156003, 1554156003, NULL, NULL, NULL, NULL, 'http://lumigear.net/loggy/grabs/1554156003.jpg', 'container', '1'),
(1554155318, 1554155318, NULL, NULL, NULL, NULL, 'http://lumigear.net/loggy/grabs/1554155318.jpg', 'container', '2');

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
) ENGINE=MyISAM AUTO_INCREMENT=170 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `logs`
--

INSERT INTO `logs` (`log_unique_id`, `log_id`, `log_img_url`, `barcode_img_url`, `grab_unique_id`, `grab_position_x`, `grab_position_y`, `grab_width`, `grab_height`, `actual_diameter`, `jas_diameter`, `jas_cbm`) VALUES
(169, 874213, 'http://lumigear.net/loggy/logs/1554168116_18_barcode.jpg', 'http://lumigear.net/loggy/logs/1554168116_18.jpg', '1554168116', 4257, 2152, 242, 242, 7.2782, 7, 0),
(168, 888646, 'http://lumigear.net/loggy/logs/1554168116_12_barcode.jpg', 'http://lumigear.net/loggy/logs/1554168116_12.jpg', '1554168116', 3685, 1836, 226, 226, 7.29032, 7, 0),
(167, 854121, 'http://lumigear.net/loggy/logs/1554168116_8_barcode.jpg', 'http://lumigear.net/loggy/logs/1554168116_8.jpg', '1554168116', 3993, 952, 274, 274, 10.6927, 10, 0),
(166, 920100, 'http://lumigear.net/loggy/logs/1554168116_5_barcode.jpg', 'http://lumigear.net/loggy/logs/1554168116_5.jpg', '1554168116', 1822, 855, 266, 266, 7.28767, 7, 0),
(165, 797464, 'http://lumigear.net/loggy/logs/1554156003_23_barcode.jpg', 'http://lumigear.net/loggy/logs/1554156003_23.jpg', '1554156003', 2957, 2695, 324, 324, 11.2696, 11, 0),
(164, 777222, 'http://lumigear.net/loggy/logs/1554156003_13_barcode.jpg', 'http://lumigear.net/loggy/logs/1554156003_13.jpg', '1554156003', 2185, 1871, 244, 244, 7.28358, 7, 0),
(163, 777946, 'http://lumigear.net/loggy/logs/1554156003_7_barcode.jpg', 'http://lumigear.net/loggy/logs/1554156003_7.jpg', '1554156003', 1695, 1225, 268, 268, 7.29252, 7, 0),
(162, 915421, 'http://lumigear.net/loggy/logs/1554155318_16_barcode.jpg', 'http://lumigear.net/loggy/logs/1554155318_16.jpg', '1554155318', 2805, 2130, 265, 265, 7.31034, 7, 0),
(161, 910101, 'http://lumigear.net/loggy/logs/1554155318_14_barcode.jpg', 'http://lumigear.net/loggy/logs/1554155318_14.jpg', '1554155318', 1741, 2277, 225, 225, 7.31707, 7, 0),
(160, 897741, 'http://lumigear.net/loggy/logs/1554155318_9_barcode.jpg', 'http://lumigear.net/loggy/logs/1554155318_9.jpg', '1554155318', 2897, 1592, 248, 248, 7.29412, 7, 0);

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
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_unique_id`, `order_number`, `customer_name`) VALUES
(1, 'ORD0000001', 'BTA'),
(2, 'ORD0000002', 'BTA');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `created_at`) VALUES
(1, 'Ed', '$2y$10$jMi.UH6VPpEysMYdod6cOuYVFDkSjboQVcTG/mOuuGHPsZnmKNjO6', '2019-03-28 08:28:00'),
(2, 'loggy', '$2y$10$PNz1c4tFN3JWXCFjDjYpz.9nfN3SYXA6ehvTkehErndg8Ata4X3AW', '2019-03-28 09:02:56');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
