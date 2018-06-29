-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Creato il: Gen 27, 2018 alle 16:34
-- Versione del server: 5.7.21-0ubuntu0.16.04.1
-- Versione PHP: 7.0.22-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hapi_development`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `cntrMunicipalities`
--

DROP TABLE IF EXISTS `cntrMunicipalities`;
CREATE TABLE `cntrMunicipalities` (
  `id` int(11) NOT NULL,
  `name` varchar(128) NOT NULL,
  `otherName` varchar(128) DEFAULT NULL,
  `municipalityProg` int(11) NOT NULL,
  `cadCode` varchar(8) NOT NULL,
  `provCapital` TINYINT(1) DEFAULT FALSE,
  `pop2011` int(11) NOT NULL,
  `metroId` INT(11) DEFAULT NULL,
  `provinceId` INT(11) NOT NULL ,
  `regionId` INT(11) NOT NULL ,
  `geoRepartitionId` INT(11) NOT NULL ,
  `createdAt` DATETIME,
  `updatedAt` DATETIME,
  `deletedAt` DATETIME
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indici per le tabelle `cntrMunicipalities`
--
ALTER TABLE `cntrMunicipalities`
  ADD PRIMARY KEY (`id`),
  ADD INDEX (`provinceId`),
  ADD INDEX (`regionId`),
  ADD INDEX (`geoRepartitionId`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `cntrMunicipalities`
--
ALTER TABLE `cntrMunicipalities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
