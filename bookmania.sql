-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: bookmania
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `book_id` int NOT NULL,
  `Bookname` varchar(255) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `Author` varchar(255) DEFAULT NULL,
  `genre` varchar(255) DEFAULT NULL,
  `poster` varchar(255) DEFAULT NULL,
  `book_pdf` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (3197104,'Living in the Light',735,'Shakti Gawain','Self-help book','./Sample_Books/Covers/Livinginthelight.jpg','./Sample_Books/Books/Living in the Light_ A guide to personal transformation ( PDFDrive ).pdf'),(30444542,'Law of Success',242,'Napoleon Hil','Self-help book','./Sample_Books/Covers/Lawofsuccess.jpg','./Sample_Books/Books/Law of Success (21st Century Edition) ( PDFDrive ).pdf'),(136931470,'Give and Take',1143,'Adam Grant','Businness Managemet','./Sample_Books/Covers/Giveandtake.jpg','./Sample_Books/Books/Give and Take_ WHY HELPING OTHERS DRIVES OUR SUCCESS ( PDFDrive ).pdf'),(334655042,'Smart Trust',301,'Greg Link','Self-help book','./Sample_Books/Covers/SmartTrust.jpg','./Sample_Books/Books/Smart Trust_ Creating Prosperity, Energy, and Joy in a Low-Trust World ( PDFDrive ).pdf'),(366982004,'Ikigai',601,'Francesc Miralles','Self-help book','./Sample_Books/Covers/Ikigai.jpg','./Sample_Books/Books/Ikigai.pdf'),(408768197,'The Alchemist',105,'Paulo Coelho','Drama','./Sample_Books/Covers/TheAlchemist.jpg','./Sample_Books/Books/The Alchemist.pdf'),(1185460522,'I Am Malala',251,'Christina Lamb','Biography','./Sample_Books/Covers/IamMalala.jpg','./Sample_Books/Books/I am Malala.pdf'),(1196929936,'Rich Dad Poor Dad',469,'Robert Kiyosaki','Self-help book','./Sample_Books/Covers/RichDadPoorDad.jpg','./Sample_Books/Books/Rich Dad Poor Dad.pdf'),(1328997796,'Everything Is F*cked',1828,'Mark Manson','Self-help book','./Sample_Books/Covers/EverythingIsF_cked.jpg','./Sample_Books/Books/Everything Is F_cked.pdf'),(1387764055,'100 ways',100,'Steve Chandler','Self-help book','./Sample_Books/Covers/100waystomotivateyourself.jpg','./Sample_Books/Books/100 ways to motivate yourself.pdf'),(1596466071,'How To Win Friends',668,'Dale Carnegie','Self-help book','./Sample_Books/Covers/Howtowinfriendsandinfluencepeople.jpg','./Sample_Books/Books/How To Win Friends and Influence People ( PDFDrive ) (1).pdf'),(1624676307,'Win Every Argument',501,'Madson Pirie','Psychology','./Sample_Books/Covers/Howtowinanyargument.jpg','./Sample_Books/Books/How to Win Every Argument ( PDFDrive ).pdf'),(1998471459,'Boundaries',1099,'Henry Cloud','Self-help book','./Sample_Books/Covers/Boundaries.jpg','./Sample_Books/Books/Boundaries_ When to Say Yes, How to Say No to Take Control of Your Life ( PDFDrive ).pdf'),(2024047480,'CRITICAL THINKING',2100,'Bruce Waller','Study Aids','./Sample_Books/Covers/CRITICALTHINKING.jpg','./Sample_Books/Books/CRITICAL THINKING_ Consider the Verdict Sixth Edition ( PDFDrive ).pdf');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boughtbooks`
--

DROP TABLE IF EXISTS `boughtbooks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boughtbooks` (
  `User_id` int NOT NULL,
  `book_id` int NOT NULL,
  `last_ch_read` int DEFAULT NULL,
  `poster` varchar(255) DEFAULT NULL,
  `book_pdf` varchar(255) DEFAULT NULL,
  `BoughtDate` date DEFAULT (curdate())
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boughtbooks`
--

LOCK TABLES `boughtbooks` WRITE;
/*!40000 ALTER TABLE `boughtbooks` DISABLE KEYS */;
INSERT INTO `boughtbooks` VALUES (517124508,30444542,NULL,'./Sample_Books/Covers/Lawofsuccess.jpg','./Sample_Books/Books/Law of Success (21st Century Edition) ( PDFDrive ).pdf','2022-11-17'),(83776742,30444542,NULL,'./Sample_Books/Covers/Lawofsuccess.jpg','./Sample_Books/Books/Law of Success (21st Century Edition) ( PDFDrive ).pdf','2022-11-18'),(83776742,408768197,NULL,'./Sample_Books/Covers/TheAlchemist.jpg','./Sample_Books/Books/The Alchemist.pdf','2022-11-18'),(83776742,1185460522,NULL,'./Sample_Books/Covers/IamMalala.jpg','./Sample_Books/Books/I am Malala.pdf','2022-11-18');
/*!40000 ALTER TABLE `boughtbooks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `featured_books`
--

DROP TABLE IF EXISTS `featured_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `featured_books` (
  `book_id` int NOT NULL,
  `Bookname` varchar(255) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `genre` varchar(255) DEFAULT NULL,
  `poster` varchar(255) DEFAULT NULL,
  `book_pdf` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `featured_books`
--

LOCK TABLES `featured_books` WRITE;
/*!40000 ALTER TABLE `featured_books` DISABLE KEYS */;
INSERT INTO `featured_books` VALUES (430946654,'One Indian Girl',209,'Chetan Bhagat',' Fiction & Literature','./Featured_Books/Covers/One_Indian_Girl.jpg','./Featured_Books/Books/One_Indian_Girl.pdf'),(571220508,'The Monk Who Sold His Ferrari',453,'Robin S. Sharma','Fiction & Literature','./Featured_Books/Covers/The_monk_who_sold_his_ferrari.jpg','./Featured_Books/Covers/The_Monk_Who_Sold_His_Ferrari.pdf'),(717963831,'The Warren Buffett Way',105,'Robert G. Hagstrom','Business & Career  Fiction & Literature  Finance','./Featured_Books/Covers/The_Warren_Buffett_Way.jpg','./Featured_Books/Books/The_Warren_Buffett_Way.pdf'),(953293191,'The Rules of Work',100,'Richard Templar','Business & Career','./Featured_Books/Covers/The_rules_of_work.jpg','./Featured_Books/Books/The_Rules_of_Work.pdf'),(1875708593,'The Girl with the Dragon Tatoo',109,'Stieg Larsson','Mystery & Crime','./Featured_Books/Covers/The_Girl_with_the_Dragon_Tattoo.jpg','./Featured_Books/Books/TheGirlwiththeDragonTattoo.pdf');
/*!40000 ALTER TABLE `featured_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `FullName` varchar(255) NOT NULL,
  `user_id` int NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `coins` int DEFAULT '500',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Aryan',83776742,'aryanpurohit6@gmail.com','password',102),('Aryan',783837992,'test@gmail.com','password',500);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-16 22:50:49
