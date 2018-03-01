CREATE DATABASE  IF NOT EXISTS `db_schedule` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `db_schedule`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 46.101.140.93    Database: db_schedule
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `schedules`
--

DROP TABLE IF EXISTS `schedules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schedules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lecture_name` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lecture_begin` time DEFAULT NULL,
  `lecture_end` time DEFAULT NULL,
  `lecture_hall` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lecture_teacher` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lecture_num` tinyint(4) DEFAULT NULL,
  `week_id` tinyint(4) DEFAULT NULL,
  `week_day` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `note` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedules`
--

LOCK TABLES `schedules` WRITE;
/*!40000 ALTER TABLE `schedules` DISABLE KEYS */;
INSERT INTO `schedules` VALUES (1,'Системная защита, лр, 1 гр.','09:40:00','11:00:00','4-54','Злобин С.В.',2,1,'Mo',''),(2,'Проф. Практика ПИ, лекция','11:25:00','12:45:00','4-51','Злобин С.В.',3,1,'Mo',''),(3,'Системная защита, лр, 2 гр.','13:10:00','14:30:00','4-54','Злобин С.В.',4,1,'Mo',''),(4,'Основы ПИ, лр, 1 гр.','09:40:00','11:00:00','4-10','Литвинов В.В.',2,1,'Tu',''),(5,'Основы ПИ, лекция','11:25:00','12:45:00','4-10','Литвинов В.В.',3,1,'Tu',''),(6,'Основы ПИ, лр, 2 гр.','13:10:00','14:30:00','4-10','Литвинов В.В.',4,1,'Tu',''),(7,'Менеджмент проектов, лр, 1 гр.','09:40:00','11:00:00','4-51','Дорош М.С.',2,1,'We',''),(8,'Модели и системы ИИ, лекция.','11:25:00','12:45:00','4-51','Дорош М.С.',3,1,'We',''),(9,'Качество ПО, лр, 1 гр.','13:10:00','14:30:00','4-54','Богдан И.В.',4,1,'We',''),(10,'Менеджмент проектов, лр, 2 гр.','13:10:00','14:30:00','4-51','Дорош М.С.',4,1,'We',''),(11,'Качество ПО, лр, 2 гр.','14:50:00','16:10:00','4-54','Богдан И.В.',5,1,'We',''),(12,'Методы организции, лр, 1 гр.','08:00:00','09:20:00','4-54','Дорош М.С.',1,1,'Th',''),(13,'Методы организции, лекция','09:40:00','11:00:00','4-54','Дорош М.С.',2,1,'Th',''),(14,'Методы организции, лр, 2 гр.','11:25:00','12:45:00','4-54','Дорош М.С.',3,1,'Th',''),(15,'Моделирование и анализ ПО, лр, 1 гр.','09:40:00','11:00:00','4-10','Стеценко И.В.',2,1,'Fr',''),(16,'Моделирование и анализ ПО, лекция','11:25:00','12:45:00','4-10','Стеценко И.В.',3,1,'Fr',''),(17,'Моделирование и анализ ПО, лекция','13:10:00','14:30:00','4-10','Стеценко И.В.',4,1,'Fr',''),(18,'Моделирование и анализ ПО, лр, 2 гр.','14:50:00','16:10:00','4-10','Стеценко И.В.',5,1,'Fr',''),(19,'Системная защита, лр, 1 гр.','09:40:00','11:00:00','4-73','Злобин С.В.',2,2,'Mo',''),(20,'Системная защита ВС, лекция','11:25:00','12:45:00','4-51','Злобин С.В.',3,2,'Mo',''),(21,'Системная защита, лр, 2 гр.','13:10:00','14:30:00','4-73','Злобин С.В.',4,2,'Mo',''),(22,'Основы ПИ, лекция','09:40:00','11:00:00','4-10','Литвинов В.В.',2,2,'Tu',''),(23,'Проф. практика ПИ, лекция','11:25:00','12:45:00','4-51','Злобин С.В.',3,2,'Tu',''),(24,'Проф. практика ПИ, лр, 1 гр.','09:40:00','11:00:00','4-54','Злобин С.В.',2,2,'We',''),(25,'Модели и системы ИИ, лр, 1 гр.','11:25:00','12:45:00','4-63','Дорош М.С.',3,2,'We',''),(26,'Проф. практика ПИ, лр, 2 гр.','11:25:00','12:45:00','4-54','Злобин С.В.',3,2,'We',''),(27,'Модели и системы ИИ, лекция','13:10:00','14:30:00','4-51','Дорош М.С.',4,2,'We',''),(28,'Модели и системы ИИ, лр, 2 гр.','14:50:00','16:10:00','4-63','Дорош М.С.',5,2,'We',''),(29,'Качество ПО, лр, 1 гр.','09:40:00','11:00:00','4-10','Богдан И.В.',2,2,'Th',''),(30,'Качество ПО, лекция','11:25:00','12:45:00','4-51','Богдан И.В.',3,2,'Th',''),(31,'Менеджмент проектов, лр, 1 гр.','13:10:00','14:30:00','4-63','Дорош М.С.',4,2,'Th',''),(32,'Качество ПО, лр, 2 гр.','13:10:00','14:30:00','4-10','Богдан И.В.',4,2,'Th',''),(33,'Менеджмент проектов, лр, 2 гр.','14:50:00','16:10:00','4-63','Дорош М.С.',5,2,'Th',''),(34,'Менеджмент проектов, лекция','09:40:00','11:00:00','4-51','Дорош М.С.',2,2,'Fr',''),(35,'Менеджмент проектов, лекция','11:25:00','12:45:00','4-51','Дорош М.С.',3,2,'Fr','');
/*!40000 ALTER TABLE `schedules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'db_schedule'
--

--
-- Dumping routines for database 'db_schedule'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-01 10:33:08
