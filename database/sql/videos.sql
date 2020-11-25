/*
 Navicat Premium Data Transfer

 Source Server         : ar
 Source Server Type    : PostgreSQL
 Source Server Version : 100014
 Source Host           : localhost:5432
 Source Catalog        : video_spider
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 100014
 File Encoding         : 65001

 Date: 23/11/2020 16:01:22
*/


-- ----------------------------
-- Table structure for videos
-- ----------------------------
DROP TABLE IF EXISTS "public"."videos";
CREATE TABLE "public"."videos" (
  "id" char(32) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "format" varchar(8) COLLATE "pg_catalog"."default" NOT NULL,
  "md5" char(32) COLLATE "pg_catalog"."default" NOT NULL,
  "local_video_path" varchar(256) COLLATE "pg_catalog"."default" NOT NULL,
  "cloud_video_path" varchar(512) COLLATE "pg_catalog"."default" NOT NULL,
  "cloud_cover_path" varchar(512) COLLATE "pg_catalog"."default" NOT NULL,
  "size" int4 NOT NULL,
  "date_created" char(19) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Primary Key structure for table videos
-- ----------------------------
ALTER TABLE "public"."videos" ADD CONSTRAINT "videos_pkey" PRIMARY KEY ("id");
