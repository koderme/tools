-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';


DROP SCHEMA IF EXISTS recruit ;


CREATE SCHEMA IF NOT EXISTS recruit DEFAULT CHARACTER SET utf8 ;
USE recruit ;

----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.status_mast ;

CREATE TABLE IF NOT EXISTS recruit.status_mast (
  status_code        VARCHAR(100) NOT NULL,          
  description VARCHAR(100),
  update_date       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (status_code)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.location_mast ;

CREATE TABLE IF NOT EXISTS recruit.location_mast (
  location_code        VARCHAR(100) NOT NULL,          
  location_description VARCHAR(100),
  update_date       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (location_code)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.client_mast ;

CREATE TABLE IF NOT EXISTS recruit.client_mast (
  client_code   VARCHAR(100) NOT NULL,          
  description   VARCHAR(100),
  addr1         VARCHAR(250),
  addr2         VARCHAR(250),
  addr3         VARCHAR(250),
  update_date   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (client_code)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.job_source_hub_mast ;

CREATE TABLE IF NOT EXISTS recruit.job_source_hub_mast (
  job_source_hub_code   VARCHAR(100) NOT NULL,          
  description           VARCHAR(100),
  update_date       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (job_source_hub_code)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.requirement ;

CREATE TABLE IF NOT EXISTS recruit.requirement (
  requirement_id     BIGINT  AUTO_INCREMENT NOT NULL,
  requirement_code   VARCHAR(100) NOT NULL,
  client_code        VARCHAR(100) NOT NULL,
  job_source_hub_code VARCHAR(100) NOT NULL,
  location_code      VARCHAR(100) NOT NULL,
  interview_addr     VARCHAR(250),
  role               VARCHAR(100) NOT NULL,
  min_ctc            SMALLINT NOT NULL,
  max_ctc            SMALLINT NOT NULL,
  min_exp            SMALLINT NOT NULL,
  max_exp            SMALLINT NOT NULL,
  number_of_positions SMALLINT NOT NULL,
  comment1           VARCHAR(500),
  comment2           VARCHAR(500),
  update_date       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (requirement_id),

  CONSTRAINT fk_requirement_jshc
    FOREIGN KEY (job_source_hub_code)
    REFERENCES recruit.job_source_hub_mast (job_source_hub_code)
    ON DELETE RESTRICT,

  CONSTRAINT fk_requirement_lc
    FOREIGN KEY (location_code)
    REFERENCES recruit.location_mast (location_code)
    ON DELETE RESTRICT)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE UNIQUE INDEX idx_requirement_rc
ON recruit.requirement (requirement_code);


----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.requirement_jd ;

CREATE TABLE IF NOT EXISTS recruit.requirement_jd (
  requirement_jd_id     BIGINT  AUTO_INCREMENT NOT NULL,
  requirement_id    BIGINT NOT NULL,
  req_jd_type       VARCHAR(50) NOT NULL, -- mandatory, optional, responsibilities
  description       VARCHAR(500) NOT NULL,
  update_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (requirement_jd_id),

  CONSTRAINT fk_requirement_jd_ri
    FOREIGN KEY (requirement_id)
    REFERENCES recruit.requirement (requirement_id)
    ON DELETE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.resume ;

CREATE TABLE IF NOT EXISTS recruit.resume (
  resume_id         BIGINT NOT NULL,
  first_name        VARCHAR(100) NOT NULL,
  middle_name       VARCHAR(100),
  last_name         VARCHAR(100),
  email_id          VARCHAR(100),
  phone1            VARCHAR(100),
  phone2            VARCHAR(100),
  recruit_hub_code  VARCHAR(100),
  current_location_code  VARCHAR(100),
  preferred_location1_code  VARCHAR(100),
  preferred_location2_code  VARCHAR(100),
  preferred_location3_code  VARCHAR(100),
  preferred_location4_code  VARCHAR(100),
  current_ctc        BIGINT,
  expected_ctc       BIGINT,
  notice_period      BIGINT,
  serving_notice     CHAR(1),
  resume_filepath   VARCHAR(500) NOT NULL,
  update_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (resume_id))

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;




----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.resume_detail ;

CREATE TABLE IF NOT EXISTS recruit.resume_detail (
  resume_id         BIGINT NOT NULL,
  part_id           BIGINT NOT NULL,
  resume_text       VARCHAR(500) NOT NULL,
  update_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (resume_id, part_id),
  CONSTRAINT fk_resume_detail_ri
    FOREIGN KEY (resume_id)
    REFERENCES recruit.resume(resume_id)
    ON DELETE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.candidate_tracker ;

CREATE TABLE IF NOT EXISTS recruit.candidate_tracker (
  requirement_id    BIGINT NOT NULL,
  resume_id         BIGINT NOT NULL,
  version_id        BIGINT NOT NULL,
  status_code       VARCHAR(100) NOT NULL,          
  valid_from        DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  valid_to          DATETIME,
  comment1          VARCHAR(250),

  PRIMARY KEY (requirement_id, resume_id, version_id),

  CONSTRAINT fk_candidate_tracker_ri
    FOREIGN KEY (requirement_id)
    REFERENCES recruit.requirement(requirement_id)
    ON DELETE RESTRICT,

  CONSTRAINT fk_candidate_tracker_rsi
    FOREIGN KEY (resume_id)
    REFERENCES recruit.resume(resume_id)
    ON DELETE RESTRICT,

  CONSTRAINT fk_candidate_tracker_sc
    FOREIGN KEY (status_code)
    REFERENCES recruit.status_mast(status_code)
    ON DELETE RESTRICT)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.req_skill;

CREATE TABLE IF NOT EXISTS recruit.req_skill(
  req_skill_id      BIGINT NOT NULL,

  requirement_id    BIGINT NOT NULL,
  part_id           BIGINT NOT NULL,

  weithage_1        SMALLINT NOT NULL,
  skill_code_1      VARCHAR(100) NOT NULL,          
  weithage_2        SMALLINT NOT NULL,
  skill_code_2      VARCHAR(100) NOT NULL,          
  weithage_3        SMALLINT NOT NULL,
  skill_code_3      VARCHAR(100) NOT NULL,          
  weithage_4        SMALLINT NOT NULL,
  skill_code_4      VARCHAR(100) NOT NULL,          
  weithage_5        SMALLINT NOT NULL,
  skill_code_5      VARCHAR(100) NOT NULL,          
  weithage_6        SMALLINT NOT NULL,
  skill_code_6      VARCHAR(100) NOT NULL,          
  weithage_7        SMALLINT NOT NULL,
  skill_code_7      VARCHAR(100) NOT NULL,          
  weithage_8        SMALLINT NOT NULL,
  skill_code_8      VARCHAR(100) NOT NULL,          
  weithage_9        SMALLINT NOT NULL,
  skill_code_9      VARCHAR(100) NOT NULL,          
  weithage_10       SMALLINT NOT NULL,
  skill_code_10     VARCHAR(100) NOT NULL,          

  weithage_11        SMALLINT NOT NULL,
  skill_code_11      VARCHAR(100) NOT NULL,          
  weithage_12        SMALLINT NOT NULL,
  skill_code_12      VARCHAR(100) NOT NULL,          
  weithage_13        SMALLINT NOT NULL,
  skill_code_13      VARCHAR(100) NOT NULL,          
  weithage_14        SMALLINT NOT NULL,
  skill_code_14      VARCHAR(100) NOT NULL,          
  weithage_15        SMALLINT NOT NULL,
  skill_code_15      VARCHAR(100) NOT NULL,          
  weithage_16        SMALLINT NOT NULL,
  skill_code_16      VARCHAR(100) NOT NULL,          
  weithage_17        SMALLINT NOT NULL,
  skill_code_17      VARCHAR(100) NOT NULL,          
  weithage_18        SMALLINT NOT NULL,
  skill_code_18      VARCHAR(100) NOT NULL,          
  weithage_19        SMALLINT NOT NULL,
  skill_code_19      VARCHAR(100) NOT NULL,          
  weithage_20        SMALLINT NOT NULL,
  skill_code_20      VARCHAR(100) NOT NULL,          

  update_date       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

  PRIMARY KEY (req_skill_id),

  CONSTRAINT fk_req_skill_ri
    FOREIGN KEY (requirement_id)
    REFERENCES recruit.requirement(requirement_id)
    ON DELETE RESTRICT)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
-- tbd
----------------------------------------------------
DROP TABLE IF EXISTS recruit.req_skill_match;

CREATE TABLE IF NOT EXISTS recruit.req_skill_match(
  req_skill_id      BIGINT NOT NULL,
  resume_id         BIGINT NOT NULL,

  match_1           CHAR(1),
  match_2           CHAR(1),
  match_3           CHAR(1),
  match_4           CHAR(1),
  match_5           CHAR(1),
  match_6           CHAR(1),
  match_7           CHAR(1),
  match_8           CHAR(1),
  match_9           CHAR(1),
  match_10          CHAR(1),

  match_11          CHAR(1),
  match_12          CHAR(1),
  match_13          CHAR(1),
  match_14          CHAR(1),
  match_15          CHAR(1),
  match_16          CHAR(1),
  match_17          CHAR(1),
  match_18          CHAR(1),
  match_19          CHAR(1),
  match_20          CHAR(1),

  update_date       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

  PRIMARY KEY (req_skill_id, resume_id),

  CONSTRAINT fk_req_skill_match_rsi
    FOREIGN KEY (req_skill_id)
    REFERENCES recruit.req_skill(req_skill_id)
    ON DELETE RESTRICT,

  CONSTRAINT fk_req_skill_match_ri
    FOREIGN KEY (resume_id)
    REFERENCES recruit.resume(resume_id)
    ON DELETE RESTRICT)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

