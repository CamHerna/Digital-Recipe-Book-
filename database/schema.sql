-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: recipebox
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes` (
  `recipe_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text,
  `ingredients` text NOT NULL,
  `instructions` text NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `image_path` varchar(255) DEFAULT NULL,
  `is_sample_data` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`recipe_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (1,'Classic Spaghetti Bolognese','A rich and savory meat sauce served over spaghetti. A timeless comfort food classic.','1 lb ground beef, 1 onion, 2 cloves garlic, 1 can crushed tomatoes, 2 tbsp olive oil, salt, pepper, spaghetti pasta.','1. Saut├⌐ chopped onion and garlic in olive oil.\n2. Add ground beef and cook until browned.\n3. Stir in crushed tomatoes.\n4. Simmer for at least 30 minutes.\n5. Serve over cooked spaghetti.','2025-10-14 16:54:37',NULL,1),(2,'Simple Chocolate Chip Cookies','The perfect soft and chewy chocolate chip cookies that are easy to make from scratch.','1 cup butter, 3/4 cup sugar, 3/4 cup brown sugar, 2 eggs, 1 tsp vanilla extract, 2 1/4 cups flour, 1 tsp baking soda, 2 cups chocolate chips.','1. Cream butter and sugars together.\n2. Beat in eggs and vanilla.\n3. Add dry ingredients.\n4. Stir in chocolate chips.\n5. Bake at 375┬░F for 9-11 minutes.','2025-10-14 16:54:37',NULL,1),(3,'Fresh Guacamole','A fresh and creamy avocado dip perfect for parties or as a topping for tacos.','3 ripe avocados, 1 lime, 1/2 red onion, 1/4 cup cilantro, 1 jalape├▒o, salt to taste.','1. Mash avocados in a bowl.\n2. Squeeze in lime juice.\n3. Stir in finely chopped onion, cilantro, and jalape├▒o.\n4. Season with salt.','2025-10-14 16:54:37',NULL,1),(4,'Perfect Scrambled Eggs','Fluffy, creamy, and simple scrambled eggs for a quick and satisfying breakfast.','3 large eggs, 3 tbsp milk, 1 tbsp butter, salt, pepper.','1. Whisk eggs, milk, salt, and pepper.\n2. Melt butter in a non-stick skillet over medium-low heat.\n3. Pour in egg mixture and cook, stirring gently, until softly set.','2025-10-14 16:54:37',NULL,1),(5,'Lemon Herb Roasted Chicken','A juicy and flavorful whole roasted chicken with bright lemon and fresh herb flavors.','1 whole chicken, 1 lemon, 4 cloves garlic, 2 tbsp olive oil, 1 tbsp fresh rosemary, 1 tbsp fresh thyme, salt, pepper.','1. Preheat oven to 425┬░F.\n2. Season chicken and stuff with lemon, garlic, and herbs.\n3. Rub outside with olive oil and herbs.\n4. Roast for 1 hour 15 minutes or until cooked through.','2025-10-14 16:54:37',NULL,1);
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-09 17:23:33
