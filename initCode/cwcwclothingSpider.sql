/*
 Navicat Premium Data Transfer

 Source Server         : 自定义数据库
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : 192.168.6.246:3306
 Source Schema         : video

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 22/06/2024 00:09:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cwcwclothing
-- ----------------------------
DROP TABLE IF EXISTS `cwcwclothing`;
CREATE TABLE `cwcwclothing`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `link` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '产品链接',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '产品标题',
  `sort` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '产品分类',
  `num` bigint(0) NULL DEFAULT NULL COMMENT '产品编号',
  `price` decimal(10, 2) NULL DEFAULT NULL COMMENT '产品价格',
  `size` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '产品尺码',
  `color` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '产品颜色',
  `color_img` varchar(3000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '产品颜色对应的图片链接',
  `intro` varchar(2000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '产品介绍',
  `main_img` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '产品首图',
  `detail_img` varchar(5000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '产品所有的详情图',
  `sale` int(0) NULL DEFAULT NULL COMMENT '产品销量',
  `evaluate_num` int(0) NULL DEFAULT NULL COMMENT '产品评价数量',
  `mark` decimal(10, 1) NULL DEFAULT NULL COMMENT '产品分数',
  `seo_title` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '产品副标题',
  `seo_intro` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '产品副介绍',
  `seo_key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '产品副关键词',
  `status` int(0) NULL DEFAULT 0 COMMENT '图片下载状态，默认为下载状态0，已下载状态1',
  `create_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `1`(`link`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cwcwclothing
-- ----------------------------
INSERT INTO `cwcwclothing` VALUES (1, 'http://127.0', '你好', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `cwcwclothing` VALUES (10, NULL, 'Nice things Waterproof hooded trench coat Dark Yellow', 'coats', NULL, 145.00, NULL, NULL, NULL, NULL, NULL, '[\'https://cwcwclothing.com/cdn/shop/files/WWS124_109_2_110x110@2x.jpg?v=1709568394\', \'https://cwcwclothing.com/cdn/shop/files/WWS124_109_5_110x110@2x.jpg?v=1709568393\', \'https://cwcwclothing.com/cdn/shop/files/WWS124_109_4_110x110@2x.jpg?v=1709568393\', \'https://cwcwclothing.com/cdn/shop/files/WWS124_109_6_110x110@2x.jpg?v=1709568391\', \'https://cwcwclothing.com/cdn/shop/files/WWS124_109_1_110x110@2x.jpg?v=1709568392\', \'https://cwcwclothing.com/cdn/shop/files/WWS124_109_7_110x110@2x.jpg?v=1709568392\']', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2024-06-22 00:08:56');

SET FOREIGN_KEY_CHECKS = 1;
