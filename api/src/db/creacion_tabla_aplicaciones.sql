CREATE DATABASE  IF NOT EXISTS `evergreen`;
USE `evergreen`;

CREATE TABLE `evergreen`.`aplicaciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `puerto` int DEFAULT NULL,
  `estado` int DEFAULT NULL,
  `tipo` int DEFAULT NULL,
  `imagen` varchar(200) DEFAULT NULL,
  `lenguaje` varchar(200) DEFAULT NULL,
  `servidor` int DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  `fecha_creacion` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;
