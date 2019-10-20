-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-10-2019 a las 19:42:48
-- Versión del servidor: 10.4.6-MariaDB
-- Versión de PHP: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `base`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `clave` int(3) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `sueldo` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`clave`, `nombre`, `sueldo`) VALUES
(1, 'pinshiaukan', 100),
(2, 'pinshiaukan2', 200),
(3, 'pinshiaukan3', 300),
(4, 'pinshiaukan4', 400),
(5, 'pinshiaukan5', 500),
(6, 'pinshiaukan6', 600),
(7, 'pinshiaukan7', 700),
(8, 'pinshiaukan8', 800),
(9, 'pinshiaukan9', 900),
(10, 'pinshiaukan10', 1000),
(11, 'pinshiaukan11', 1100),
(12, 'pinshiaukan12', 1200),
(13, 'pinshiaukan13', 1300),
(14, 'pinshiaukan14', 1400);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`clave`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
