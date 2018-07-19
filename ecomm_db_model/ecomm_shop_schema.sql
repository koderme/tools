-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';



DROP SCHEMA IF EXISTS ecomm_shop ;


CREATE SCHEMA IF NOT EXISTS ecomm_shop DEFAULT CHARACTER SET utf8 ;
USE ecomm_shop ;


----------------------------------------------------
-- Admin
----------------------------------------------------
----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.shop_detail ;

CREATE TABLE IF NOT EXISTS ecomm_shop.shop_detail (
  shop_name         VARCHAR(100) NOT NULL,
  description       VARCHAR(500) NOT NULL,
  motto             VARCHAR(500) NOT NULL,
  updated_by        VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (shop_name))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;




----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.shop_artefact ;

CREATE TABLE IF NOT EXISTS ecomm_shop.shop_artefact (
  artefact_name     VARCHAR(100) NOT NULL,
  file_path         VARCHAR(100) NOT NULL,
  updated_by        VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (artefact_name))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
-- Customer management
----------------------------------------------------
----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.payment_type_code ;

CREATE TABLE IF NOT EXISTS ecomm_shop.payment_type_code (
  payment_type_code VARCHAR(50) NOT NULL,
  updated_by         VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_type_code))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.customer ;

CREATE TABLE IF NOT EXISTS ecomm_shop.customer (
  customer_id      BIGINT NOT NULL,
  login_id         VARCHAR(100) NOT NULL,
  password         VARCHAR(500) NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE UNIQUE INDEX idx_customer_li
ON ecomm_shop.customer (login_id);

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.customer_profile ;

CREATE TABLE IF NOT EXISTS ecomm_shop.customer_profile (
  customer_id      BIGINT NOT NULL,
  gender           CHAR(1) DEFAULT 'Y',
  prefix           VARCHAR(10) ,
  first_name       VARCHAR(100) NOT NULL,
  middle_name      VARCHAR(100) ,
  last_name        VARCHAR(100) NOT NULL,
  dob              DATE,
  phone_number     VARCHAR(20),
  phone_verified   CHAR(1) DEFAULT 'Y',
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id),

  CONSTRAINT fk_customer_profile_ci
    FOREIGN KEY (customer_id)
    REFERENCES ecomm_shop.customer (customer_id)
    ON DELETE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE INDEX idx_customer_profile_flp
ON ecomm_shop.customer_profile (first_name, last_name, phone_number);

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.customer_address ;

CREATE TABLE IF NOT EXISTS ecomm_shop.customer_address (
  customer_address_id    BIGINT NOT NULL,
  customer_id            BIGINT NOT NULL,
  address_type           CHAR(1) NOT NULL,
  apartment_building     VARCHAR(100) NOT NULL,
  first_line             VARCHAR(100) NOT NULL,
  second_line            VARCHAR(100) NOT NULL,
  street                 VARCHAR(100) NOT NULL,
  city                   VARCHAR(100) NOT NULL,
  state                  VARCHAR(100) NOT NULL,
  country                VARCHAR(100) NOT NULL,
  zip_code               VARCHAR(6) NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_address_id),
  CONSTRAINT fk_customer_address_ci
    FOREIGN KEY (customer_id)
    REFERENCES ecomm_shop.customer (customer_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE INDEX idx_customer_address_ci
ON ecomm_shop.customer_address (customer_id);

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.customer_payment_info ;

CREATE TABLE IF NOT EXISTS ecomm_shop.customer_payment_info (
  customer_payment_info_id      BIGINT NOT NULL,
  customer_id                   BIGINT NOT NULL,
  payment_type_code             VARCHAR(50) NOT NULL,
  payment_number                VARCHAR(50) NOT NULL,
  expiry_date_mm_yy             VARCHAR(6) NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date                  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_payment_info_id),

  CONSTRAINT fk_customer_payment_info_ci
    FOREIGN KEY (customer_id)
    REFERENCES ecomm_shop.customer (customer_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_customer_payment_info_ptc
    FOREIGN KEY (payment_type_code)
    REFERENCES ecomm_shop.payment_type (payment_type_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE INDEX idx_customer_payment_info_ci
ON ecomm_shop.customer_payment_info (customer_id);

----------------------------------------------------
-- Product management
----------------------------------------------------
----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.unit_code ;

CREATE TABLE IF NOT EXISTS ecomm_shop.unit_code (
  unit_code         VARCHAR(50) NOT NULL,
  updated_by         VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (unit_code))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.discount_type_code ;

CREATE TABLE IF NOT EXISTS ecomm_shop.discount_type_code (
  discount_type_code VARCHAR(50) NOT NULL,
  updated_by         VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (discount_type_code))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.product_category_code ;

CREATE TABLE IF NOT EXISTS ecomm_shop.product_category_code (
  product_category_code  VARCHAR(50) NOT NULL,
  updated_by             VARCHAR(50) NOT NULL default 'system',
  updated_date           DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_category_code))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.product_sub_category_code;

CREATE TABLE IF NOT EXISTS ecomm_shop.product_sub_category_code(
  product_sub_category_code VARCHAR(100) NOT NULL,
  updated_by                VARCHAR(50) NOT NULL default 'system',
  updated_date              DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_sub_category_code))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.product;

CREATE TABLE IF NOT EXISTS ecomm_shop.product (
  product_id              BIGINT NOT NULL,
  product_code            VARCHAR(100) NOT NULL,
  description             VARCHAR(500),
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE UNIQUE INDEX idx_product_pc
ON ecomm_shop.product (product_code);

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.product_category_rel ;

CREATE TABLE IF NOT EXISTS ecomm_shop.product_category_rel (
  product_id           BIGINT NOT NULL,
  iteration            BIGINT NOT NULL,
  category_code1       VARCHAR(50) NOT NULL,
  category_code2       VARCHAR(50),
  category_code3       VARCHAR(50),
  sub_category_code1   VARCHAR(50) NOT NULL,
  sub_category_code2   VARCHAR(50),
  sub_category_code3   VARCHAR(50),

  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, iteration),

  CONSTRAINT fk_product_category_rel_pi
    FOREIGN KEY (product_id)
    REFERENCES ecomm_shop.product(product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_product_category_rel_cc1
    FOREIGN KEY (category_code1)
    REFERENCES ecomm_shop.product_category_code(product_category_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_product_category_rel_scc1
    FOREIGN KEY (category_code1)
    REFERENCES ecomm_shop.product_sub_category(product_sub_category_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE INDEX idx_product_category_rel_cc123
ON ecomm_shop.product_category_rel (category_code1, category_code2, category_code3);

CREATE INDEX idx_product_category_rel_scc123
ON ecomm_shop.product_category_rel (sub_category_code1, sub_category_code2, sub_category_code3);

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.attribute_key_code ;

CREATE TABLE IF NOT EXISTS ecomm_shop.attribute_key_code (
  attribute_key_code       VARCHAR(50) NOT NULL,
  description              VARCHAR(500) NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (attribute_key_code))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.product_attribute_kv ;

CREATE TABLE IF NOT EXISTS ecomm_shop.product_attribute_kv (
  product_id            BIGINT NOT NULL,
  attribute_key_code    VARCHAR(50) NOT NULL,
  attribute_value       VARCHAR(100) NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, attribute_key_code),

  CONSTRAINT fk_product_attribute_kv_pi
    FOREIGN KEY (product_id)
    REFERENCES ecomm_shop.product(product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_product_attribute_kv_akc
    FOREIGN KEY (attribute_key_code)
    REFERENCES ecomm_shop.attribute_key_code(attribute_key_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
-- Vendor management
----------------------------------------------------
----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.vendor ;

CREATE TABLE IF NOT EXISTS ecomm_shop.vendor (
  vendor_id         BIGINT NOT NULL,
  vendor_name       VARCHAR(100) NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (vendor_id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.vendor_detail ;

CREATE TABLE IF NOT EXISTS ecomm_shop.vendor_detail (
  vendor_id         BIGINT NOT NULL,
  gst_number        VARCHAR(20) NOT NULL,
  phone_number1     VARCHAR(20) NOT NULL,
  phone_number2     VARCHAR(20) NOT NULL,
  phone_number3     VARCHAR(20) NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (vendor_id),
  CONSTRAINT fk_vendor_detail_vi
    FOREIGN KEY (vendor_id)
    REFERENCES ecomm_shop.vendor (vendor_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.vendor_product;

CREATE TABLE IF NOT EXISTS ecomm_shop.vendor_product (
  vendor_product_id    BIGINT NOT NULL,
  vendor_id            BIGINT NOT NULL,
  product_id           BIGINT NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  valid_from           DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  valid_to             DATETIME NOT NULL DEFAULT '9999-12-31',
  PRIMARY KEY (vendor_product_id),
  CONSTRAINT fk_vendor_product_pi
    FOREIGN KEY (product_id)
    REFERENCES ecomm_shop.product(product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_vendor_product_vi
    FOREIGN KEY (vendor_id)
    REFERENCES ecomm_shop.vendor (vendor_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE UNIQUE INDEX idx_vendor_product_vipi
ON ecomm_shop.vendor_product (vendor_id, product_id, valid_from);

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.vendor_product_image ;

CREATE TABLE IF NOT EXISTS ecomm_shop.vendor_product_image (
  vendor_product_id     BIGINT NOT NULL,
  iteration             BIGINT NOT NULL,
  image_path            VARCHAR(500) NOT NULL,
  updated_by            VARCHAR(50) NOT NULL default 'system',
  updated_date          DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

  PRIMARY KEY (vendor_product_id, iteration),
  CONSTRAINT fk_vendor_product_image_pi
    FOREIGN KEY (vendor_product_id)
    REFERENCES ecomm_shop.vendor_product(vendor_product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
-- Price management
----------------------------------------------------
----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.currency_code ;

CREATE TABLE IF NOT EXISTS ecomm_shop.currency_code (
  currency_code          VARCHAR(10) NOT NULL,
  updated_by             VARCHAR(50) NOT NULL default 'system',
  updated_date           DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (currency_code))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.currency_rate ;

CREATE TABLE IF NOT EXISTS ecomm_shop.currency_rate (
  currency_rate_id          BIGINT NOT NULL,
  currency_code             VARCHAR(10) NOT NULL,
  vid                       BIGINT NOT NULL,
  is_latest_vid             CHAR(1) NOT NULL DEFAULT 'Y',
  conversion_rate_to_inr    DECIMAL(15,5) NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  valid_from                DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  valid_to                  DATETIME NOT NULL DEFAULT '9999-12-31',
  PRIMARY KEY (currency_code, vid),

  CONSTRAINT fk_currency_rate_cc
    FOREIGN KEY (currency_code)
    REFERENCES ecomm_shop.currency_code(currency_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.vendor_product_price ;

CREATE TABLE IF NOT EXISTS ecomm_shop.vendor_product_price (
  vendor_product_id         BIGINT NOT NULL,
  vid                       BIGINT NOT NULL,
  is_latest_vid             CHAR(1) NOT NULL DEFAULT 'Y',
  unit_code                 VARCHAR(50) NOT NULL,
  price                     DECIMAL(15,2) NOT NULL,
  currency_code             VARCHAR(10) NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  valid_from                DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  valid_to                  DATETIME NOT NULL DEFAULT '9999-12-31',
  PRIMARY KEY (vendor_product_id, vid),

  CONSTRAINT fk_vendor_product_price_vpi
    FOREIGN KEY (vendor_product_id)
    REFERENCES ecomm_shop.vendor_product(vendor_product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_vendor_product_price_uc
    FOREIGN KEY (unit_code)
    REFERENCES ecomm_shop.unit_code(unit_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_vendor_product_price_cc
    FOREIGN KEY (currency_code)
    REFERENCES ecomm_shop.currency_code(currency_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.vendor_product_discount ;

CREATE TABLE IF NOT EXISTS ecomm_shop.vendor_product_discount (
  vendor_product_id         BIGINT NOT NULL,
  vid                       BIGINT NOT NULL,
  is_latest_vid             CHAR(1) NOT NULL DEFAULT 'Y',
  discount_value            INT NOT NULL,
  discount_type_code        VARCHAR(50) NOT NULL,
  updated_by                VARCHAR(50) NOT NULL default 'system',
  valid_from                DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  valid_to                  DATETIME NOT NULL DEFAULT '9999-12-31',
  PRIMARY KEY (vendor_product_id, vid),

  CONSTRAINT fk_vendor_product_discount_vpi
    FOREIGN KEY (vendor_product_id)
    REFERENCES ecomm_shop.vendor_product(vendor_product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_vendor_product_discount_dtc
    FOREIGN KEY (discount_type_code)
    REFERENCES ecomm_shop.discount_type_code(discount_type_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
-- Inventory management
----------------------------------------------------

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.inventory_transaction ;

CREATE TABLE IF NOT EXISTS ecomm_shop.inventory_transaction (
  inventory_transaction_id       BIGINT NOT NULL,
  vendor_product_id              BIGINT NOT NULL,
  quantity                       DECIMAL(10,5) NOT NULL,
  unit_code                      VARCHAR(50) NOT NULL,
  db_cr_ind                      CHAR(1) NOT NULL,
  order_id                       VARCHAR(25),
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (inventory_transaction_id),

  CONSTRAINT fk_inventory_transaction_vpi
    FOREIGN KEY (vendor_product_id)
    REFERENCES ecomm_shop.vendor_product(vendor_product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_inventory_transaction_uc
    FOREIGN KEY (unit_code)
    REFERENCES ecomm_shop.unit_code(unit_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE UNIQUE INDEX idx_inventory_transaction_vpi
ON ecomm_shop.inventory_transaction (vendor_product_id);

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.inventory_asof ;

CREATE TABLE IF NOT EXISTS ecomm_shop.inventory_asof (
  vendor_product_id        BIGINT NOT NULL,
  asof_date                DATE NOT NULL,
  quantity                 DECIMAL(10,5) NOT NULL,
  updated_by        VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (vendor_product_id, asof_date),

  CONSTRAINT fk_inventory_asof_vpi
    FOREIGN KEY (vendor_product_id)
    REFERENCES ecomm_shop.vendor_product(vendor_product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
-- Order management
----------------------------------------------------
----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.buy_order ;

CREATE TABLE IF NOT EXISTS ecomm_shop.buy_order (
  buy_order_id         VARCHAR(25) NOT NULL,
  customer_id          BIGINT NOT NULL,
  billing_address_id   BIGINT NOT NULL,
  shipping_address_id  BIGINT NOT NULL,
  payment_info_id  BIGINT NOT NULL,
  updated_by       VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (buy_order_id),

  CONSTRAINT fk_buy_order_ci
    FOREIGN KEY (customer_id)
    REFERENCES ecomm_shop.customer(customer_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_buy_order_bai
    FOREIGN KEY (billing_address_id)
    REFERENCES ecomm_shop.customer_address(customer_address_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_buy_order_sai
    FOREIGN KEY (shipping_address_id)
    REFERENCES ecomm_shop.customer_address(customer_address_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_buy_order_pi
    FOREIGN KEY (payment_info_id)
    REFERENCES ecomm_shop.customer_payment_info(customer_payment_info_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE UNIQUE INDEX idx_buy_buy_order_ci
ON ecomm_shop.buy_order (customer_id);

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.buy_order_detail ;

CREATE TABLE IF NOT EXISTS ecomm_shop.buy_order_detail (
  buy_order_id             VARCHAR(25) NOT NULL,
  vendor_product_id BIGINT NOT NULL,
  quantity          DECIMAL(10,5) NOT NULL,
  price_per_unit    DECIMAL(10,2) NOT NULL,
  price             DECIMAL(10,2) NOT NULL,
  discount          DECIMAL(10,2) NOT NULL,
  final_price       DECIMAL(10,2) NOT NULL,
  gst_component     DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (buy_order_id, vendor_product_id),

  CONSTRAINT fk_buy_order_detail_boi
    FOREIGN KEY (buy_order_id)
    REFERENCES ecomm_shop.buy_order(buy_order_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_buy_order_detail_vpi
    FOREIGN KEY (vendor_product_id)
    REFERENCES ecomm_shop.vendor_product(vendor_product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.cancel_order ;

CREATE TABLE IF NOT EXISTS ecomm_shop.cancel_order (
  cancel_order_id   VARCHAR(25) NOT NULL,
  buy_order_id      VARCHAR(25) NOT NULL,
  updated_by        VARCHAR(50) NOT NULL default 'system',
  updated_date      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (cancel_order_id),

  CONSTRAINT fk_cancel_order_boi
    FOREIGN KEY (buy_order_id)
    REFERENCES ecomm_shop.buy_order(buy_order_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE UNIQUE INDEX idx_cancel_order_ooi
ON ecomm_shop.cancel_order (buy_order_id);

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.cancel_order_detail ;

CREATE TABLE IF NOT EXISTS ecomm_shop.cancel_order_detail (
  cancel_order_id   VARCHAR(25) NOT NULL,
  vendor_product_id BIGINT NOT NULL,
  quantity          DECIMAL(10,5) NOT NULL,
  price_per_unit    DECIMAL(10,2) NOT NULL,
  final_price       DECIMAL(10,2) NOT NULL,
  gst_component     DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (cancel_order_id, vendor_product_id),

  CONSTRAINT fk_cancel_order_detail_coi
    FOREIGN KEY (cancel_order_id)
    REFERENCES ecomm_shop.cancel_order(cancel_order_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,

  CONSTRAINT fk_cancel_order_detail_vpi
    FOREIGN KEY (vendor_product_id)
    REFERENCES ecomm_shop.vendor_product(vendor_product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE UNIQUE INDEX idx_cancel_order_detail_vpi
ON ecomm_shop.cancel_order_detail (vendor_product_id);


----------------------------------------------------
-- Order workflow
----------------------------------------------------
----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.wf_event_code;

CREATE TABLE IF NOT EXISTS ecomm_shop.wf_event_code (
  wf_event_code      VARCHAR(50) NOT NULL,
  updated_by         VARCHAR(50) NOT NULL default 'system',
  updated_date       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (wf_event_code))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.wf_state_code;

CREATE TABLE IF NOT EXISTS ecomm_shop.wf_state (
  wf_state_code       VARCHAR(50) NOT NULL,
  updated_by          VARCHAR(50) NOT NULL default 'system',
  updated_date        DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (wf_state_code))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

----------------------------------------------------
DROP TABLE IF EXISTS ecomm_shop.workflow_status ;

CREATE TABLE IF NOT EXISTS ecomm_shop.workflow_status (
  vendor_product_id         BIGINT NOT NULL,
  wf_event_code             VARCHAR(50) NOT NULL,
  event_id                  VARCHAR(100) NOT NULL,
  vid                       BIGINT NOT NULL,
  is_latest_vid             CHAR(1) NOT NULL DEFAULT 'Y',
  wf_state_code             VARCHAR(50) NOT NULL,
  valid_from                DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  valid_to                  DATETIME NOT NULL DEFAULT '9999-12-31',
  PRIMARY KEY (event_id, vid),

  CONSTRAINT fk_workflow_status_wsc
    FOREIGN KEY (wf_state_code)
    REFERENCES ecomm_shop.wf_state_code(wf_state_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE INDEX idx_workflow_status_vpi
ON ecomm_shop.workflow_status (vendor_product_id)
