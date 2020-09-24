CREATE DATABASE  IF NOT EXISTS `evergreen`
USE `evergreen`;

CREATE TABLE `evergreen`.`aplicaciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `puerto` int DEFAULT NULL,
  `estado` int DEFAULT NULL,
  `tipo` int DEFAULT NULL,
  `lenguaje` varchar(200) DEFAULT NULL,
  `servidor` int DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  `fecha_creacion` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

INSERT INTO `evergreen`.`aplicaciones` (`nombre`, `puerto`, `estado`, `tipo`, `lenguaje`, `servidor`, `version`, `fecha_creacion`, `fecha_actualizacion`) VALUES ('API Aplicaciones', '3000', '1', '1', 'flask - python', '1', '1.0.0', now(), now());
