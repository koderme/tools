-- ---------------------------
insert into ecomm_shop.product_category_code (product_category_code )
select  'cat-code-0000'  from dual union
select  'cat-code-0001'  from dual union
select  'cat-code-0002'  from dual union
select  'cat-code-0003'  from dual union
select  'cat-code-0004'  from dual union
select  'cat-code-0005'  from dual union
select  'cat-code-0006'  from dual union
select  'cat-code-0007'  from dual union
select  'cat-code-0008'  from dual union
select  'cat-code-0009'  from dual ;
-- ---------------------------
insert into ecomm_shop.product_sub_category_code (product_sub_category_code )
select  'sub-cat-code-0000'  from dual union
select  'sub-cat-code-0001'  from dual union
select  'sub-cat-code-0002'  from dual union
select  'sub-cat-code-0003'  from dual union
select  'sub-cat-code-0004'  from dual union
select  'sub-cat-code-0005'  from dual union
select  'sub-cat-code-0006'  from dual union
select  'sub-cat-code-0007'  from dual union
select  'sub-cat-code-0008'  from dual union
select  'sub-cat-code-0009'  from dual ;
-- ---------------------------
insert into ecomm_shop.attribute_key_code (attribute_key_code,description )
select  'attr-key-code-0000', 'attr-desc-0000000000000000'  from dual union
select  'attr-key-code-0001', 'attr-desc-0000000000000001'  from dual union
select  'attr-key-code-0002', 'attr-desc-0000000000000002'  from dual union
select  'attr-key-code-0003', 'attr-desc-0000000000000003'  from dual union
select  'attr-key-code-0004', 'attr-desc-0000000000000004'  from dual union
select  'attr-key-code-0005', 'attr-desc-0000000000000005'  from dual union
select  'attr-key-code-0006', 'attr-desc-0000000000000006'  from dual union
select  'attr-key-code-0007', 'attr-desc-0000000000000007'  from dual union
select  'attr-key-code-0008', 'attr-desc-0000000000000008'  from dual union
select  'attr-key-code-0009', 'attr-desc-0000000000000009'  from dual ;
-- ---------------------------
insert into ecomm_shop.payment_type_code (payment_type_code )
select  'PTC_CREDIT_CARD'  from dual ;
-- ---------------------------
insert into ecomm_shop.currency_code (currency_code )
select  'INR'  from dual ;
-- ---------------------------
insert into ecomm_shop.unit_code (unit_code )
select  'UC_1'  from dual ;
-- ---------------------------
insert into ecomm_shop.discount_type_code (discount_type_code )
select  'DT_PERCENT'  from dual union
select  'DT_PERCENT'  from dual union
select  'DT_PERCENT'  from dual union
select  'DT_PERCENT'  from dual union
select  'DT_PERCENT'  from dual union
select  'DT_PERCENT'  from dual union
select  'DT_PERCENT'  from dual union
select  'DT_PERCENT'  from dual union
select  'DT_PERCENT'  from dual union
select  'DT_PERCENT'  from dual ;
-- ---------------------------
insert into ecomm_shop.shop_artefact (artefact_name,file_path )
select  'artefact-00', '/var/tmp/'  from dual ;
-- ---------------------------
insert into ecomm_shop.shop_detail (shop_name,description,motto )
select  'HealtyOptions Inc', 'HealtyOptions Inc', 'live healthy...live long'  from dual ;
-- ---------------------------
insert into ecomm_shop.customer (customer_id,login_id,password )
select  9990000, 'cust_000', 'pass000'  from dual union
select  9990001, 'cust_001', 'pass001'  from dual union
select  9990002, 'cust_002', 'pass002'  from dual union
select  9990003, 'cust_003', 'pass003'  from dual union
select  9990004, 'cust_004', 'pass004'  from dual union
select  9990005, 'cust_005', 'pass005'  from dual union
select  9990006, 'cust_006', 'pass006'  from dual union
select  9990007, 'cust_007', 'pass007'  from dual union
select  9990008, 'cust_008', 'pass008'  from dual union
select  9990009, 'cust_009', 'pass009'  from dual ;
-- ---------------------------
insert into ecomm_shop.customer_profile (customer_id,dob,first_name,gender,last_name,middle_name,phone_number,phone_verified )
select  9990000, CURDATE(), 'f-00000', 'M', 'l-00000', '0', '+91 0000000000', 'N'  from dual union
select  9990001, CURDATE(), 'f-00001', 'M', 'l-00001', '1', '+91 0000000001', 'N'  from dual union
select  9990002, CURDATE(), 'f-00002', 'M', 'l-00002', '2', '+91 0000000002', 'N'  from dual union
select  9990003, CURDATE(), 'f-00003', 'M', 'l-00003', '3', '+91 0000000003', 'N'  from dual union
select  9990004, CURDATE(), 'f-00004', 'M', 'l-00004', '4', '+91 0000000004', 'N'  from dual union
select  9990005, CURDATE(), 'f-00005', 'M', 'l-00005', '5', '+91 0000000005', 'N'  from dual union
select  9990006, CURDATE(), 'f-00006', 'M', 'l-00006', '6', '+91 0000000006', 'N'  from dual union
select  9990007, CURDATE(), 'f-00007', 'M', 'l-00007', '7', '+91 0000000007', 'N'  from dual union
select  9990008, CURDATE(), 'f-00008', 'M', 'l-00008', '8', '+91 0000000008', 'N'  from dual union
select  9990009, CURDATE(), 'f-00009', 'M', 'l-00009', '9', '+91 0000000009', 'N'  from dual ;
-- ---------------------------
insert into ecomm_shop.customer_address (customer_address_id,customer_id,address_type,apartment_building,first_line,second_line,street,city,state,country,zip_code )
select  9990000, 9990000, 'R', 'Apt-000', ' ', ' ', '90 feet rd', 'City-000', 'MH', 'India', 400000  from dual union
select  9990001, 9990001, 'R', 'Apt-001', ' ', ' ', '90 feet rd', 'City-001', 'MH', 'India', 400001  from dual union
select  9990002, 9990002, 'R', 'Apt-002', ' ', ' ', '90 feet rd', 'City-002', 'MH', 'India', 400002  from dual union
select  9990003, 9990003, 'R', 'Apt-003', ' ', ' ', '90 feet rd', 'City-003', 'MH', 'India', 400003  from dual union
select  9990004, 9990004, 'R', 'Apt-004', ' ', ' ', '90 feet rd', 'City-004', 'MH', 'India', 400004  from dual union
select  9990005, 9990005, 'R', 'Apt-005', ' ', ' ', '90 feet rd', 'City-005', 'MH', 'India', 400005  from dual union
select  9990006, 9990006, 'R', 'Apt-006', ' ', ' ', '90 feet rd', 'City-006', 'MH', 'India', 400006  from dual union
select  9990007, 9990007, 'R', 'Apt-007', ' ', ' ', '90 feet rd', 'City-007', 'MH', 'India', 400007  from dual union
select  9990008, 9990008, 'R', 'Apt-008', ' ', ' ', '90 feet rd', 'City-008', 'MH', 'India', 400008  from dual union
select  9990009, 9990009, 'R', 'Apt-009', ' ', ' ', '90 feet rd', 'City-009', 'MH', 'India', 400009  from dual ;
-- ---------------------------
insert into ecomm_shop.customer_payment_info (customer_payment_info_id,customer_id,payment_type_code,payment_number,expiry_date_mm_yy )
select  9990000, 9990000, 'credit_card', '0000000000000000', '122020'  from dual union
select  9990001, 9990001, 'credit_card', '0000000000000001', '122020'  from dual union
select  9990002, 9990002, 'credit_card', '0000000000000002', '122020'  from dual union
select  9990003, 9990003, 'credit_card', '0000000000000003', '122020'  from dual union
select  9990004, 9990004, 'credit_card', '0000000000000004', '122020'  from dual union
select  9990005, 9990005, 'credit_card', '0000000000000005', '122020'  from dual union
select  9990006, 9990006, 'credit_card', '0000000000000006', '122020'  from dual union
select  9990007, 9990007, 'credit_card', '0000000000000007', '122020'  from dual union
select  9990008, 9990008, 'credit_card', '0000000000000008', '122020'  from dual union
select  9990009, 9990009, 'credit_card', '0000000000000009', '122020'  from dual ;
-- ---------------------------
insert into ecomm_shop.product (product_id,product_code,description )
select  9990000, 'pc-000', 'prod-desc-0000000000000000'  from dual union
select  9990001, 'pc-001', 'prod-desc-0000000000000001'  from dual union
select  9990002, 'pc-002', 'prod-desc-0000000000000002'  from dual union
select  9990003, 'pc-003', 'prod-desc-0000000000000003'  from dual union
select  9990004, 'pc-004', 'prod-desc-0000000000000004'  from dual union
select  9990005, 'pc-005', 'prod-desc-0000000000000005'  from dual union
select  9990006, 'pc-006', 'prod-desc-0000000000000006'  from dual union
select  9990007, 'pc-007', 'prod-desc-0000000000000007'  from dual union
select  9990008, 'pc-008', 'prod-desc-0000000000000008'  from dual union
select  9990009, 'pc-009', 'prod-desc-0000000000000009'  from dual ;
-- ---------------------------
insert into ecomm_shop.product_attribute_kv (product_id,attribute_key_code,attribute_value )
select  9990000, 'attr-key-code-0000', 'attr-val0000'  from dual union
select  9990001, 'attr-key-code-0001', 'attr-val0001'  from dual union
select  9990002, 'attr-key-code-0002', 'attr-val0002'  from dual union
select  9990003, 'attr-key-code-0003', 'attr-val0003'  from dual union
select  9990004, 'attr-key-code-0004', 'attr-val0004'  from dual union
select  9990005, 'attr-key-code-0005', 'attr-val0005'  from dual union
select  9990006, 'attr-key-code-0006', 'attr-val0006'  from dual union
select  9990007, 'attr-key-code-0007', 'attr-val0007'  from dual union
select  9990008, 'attr-key-code-0008', 'attr-val0008'  from dual union
select  9990009, 'attr-key-code-0009', 'attr-val0009'  from dual ;
-- ---------------------------
insert into ecomm_shop.product_category_rel (product_id,iteration,category_code1,category_code2,category_code3,sub_category_code1,sub_category_code2,sub_category_code3 )
select  9990000, 1, 'cat-code-0000', 'cat-code-0000', 'cat-code-0000', 'sub-cat-code-0000', 'sub-cat-code-0000', 'sub-cat-code-0000'  from dual union
select  9990001, 1, 'cat-code-0001', 'cat-code-0001', 'cat-code-0001', 'sub-cat-code-0001', 'sub-cat-code-0001', 'sub-cat-code-0001'  from dual union
select  9990002, 1, 'cat-code-0002', 'cat-code-0002', 'cat-code-0002', 'sub-cat-code-0002', 'sub-cat-code-0002', 'sub-cat-code-0002'  from dual union
select  9990003, 1, 'cat-code-0003', 'cat-code-0003', 'cat-code-0003', 'sub-cat-code-0003', 'sub-cat-code-0003', 'sub-cat-code-0003'  from dual union
select  9990004, 1, 'cat-code-0004', 'cat-code-0004', 'cat-code-0004', 'sub-cat-code-0004', 'sub-cat-code-0004', 'sub-cat-code-0004'  from dual union
select  9990005, 1, 'cat-code-0005', 'cat-code-0005', 'cat-code-0005', 'sub-cat-code-0005', 'sub-cat-code-0005', 'sub-cat-code-0005'  from dual union
select  9990006, 1, 'cat-code-0006', 'cat-code-0006', 'cat-code-0006', 'sub-cat-code-0006', 'sub-cat-code-0006', 'sub-cat-code-0006'  from dual union
select  9990007, 1, 'cat-code-0007', 'cat-code-0007', 'cat-code-0007', 'sub-cat-code-0007', 'sub-cat-code-0007', 'sub-cat-code-0007'  from dual union
select  9990008, 1, 'cat-code-0008', 'cat-code-0008', 'cat-code-0008', 'sub-cat-code-0008', 'sub-cat-code-0008', 'sub-cat-code-0008'  from dual union
select  9990009, 1, 'cat-code-0009', 'cat-code-0009', 'cat-code-0009', 'sub-cat-code-0009', 'sub-cat-code-0009', 'sub-cat-code-0009'  from dual ;
-- ---------------------------
insert into ecomm_shop.vendor (vendor_id,vendor_name )
select  9990000, 'vend-0000'  from dual union
select  9990001, 'vend-0001'  from dual union
select  9990002, 'vend-0002'  from dual union
select  9990003, 'vend-0003'  from dual union
select  9990004, 'vend-0004'  from dual union
select  9990005, 'vend-0005'  from dual union
select  9990006, 'vend-0006'  from dual union
select  9990007, 'vend-0007'  from dual union
select  9990008, 'vend-0008'  from dual union
select  9990009, 'vend-0009'  from dual ;
-- ---------------------------
insert into ecomm_shop.vendor_detail (vendor_id,gst_number,phone_number1,phone_number2,phone_number3 )
select  9990000, 'GST-0000000', '+91 0000000000', '+91 0000000000', '+91 0000000000'  from dual union
select  9990001, 'GST-0000001', '+91 0000000001', '+91 0000000001', '+91 0000000001'  from dual union
select  9990002, 'GST-0000002', '+91 0000000002', '+91 0000000002', '+91 0000000002'  from dual union
select  9990003, 'GST-0000003', '+91 0000000003', '+91 0000000003', '+91 0000000003'  from dual union
select  9990004, 'GST-0000004', '+91 0000000004', '+91 0000000004', '+91 0000000004'  from dual union
select  9990005, 'GST-0000005', '+91 0000000005', '+91 0000000005', '+91 0000000005'  from dual union
select  9990006, 'GST-0000006', '+91 0000000006', '+91 0000000006', '+91 0000000006'  from dual union
select  9990007, 'GST-0000007', '+91 0000000007', '+91 0000000007', '+91 0000000007'  from dual union
select  9990008, 'GST-0000008', '+91 0000000008', '+91 0000000008', '+91 0000000008'  from dual union
select  9990009, 'GST-0000009', '+91 0000000009', '+91 0000000009', '+91 0000000009'  from dual ;
-- ---------------------------
insert into ecomm_shop.vendor_product (vendor_product_id,vendor_id,product_id )
select  9990000, 9990000, 9990000  from dual union
select  9990001, 9990001, 9990001  from dual union
select  9990002, 9990002, 9990002  from dual union
select  9990003, 9990003, 9990003  from dual union
select  9990004, 9990004, 9990004  from dual union
select  9990005, 9990005, 9990005  from dual union
select  9990006, 9990006, 9990006  from dual union
select  9990007, 9990007, 9990007  from dual union
select  9990008, 9990008, 9990008  from dual union
select  9990009, 9990009, 9990009  from dual ;
-- ---------------------------
insert into ecomm_shop.vendor_product_price (vendor_product_id,vid,is_latest_vid,unit_code,price,currency_code )
select  9990000, 1, 'Y', 'UC_1', 10.12, 'INR'  from dual union
select  9990001, 1, 'Y', 'UC_1', 10.12, 'INR'  from dual union
select  9990002, 1, 'Y', 'UC_1', 10.12, 'INR'  from dual union
select  9990003, 1, 'Y', 'UC_1', 10.12, 'INR'  from dual union
select  9990004, 1, 'Y', 'UC_1', 10.12, 'INR'  from dual union
select  9990005, 1, 'Y', 'UC_1', 10.12, 'INR'  from dual union
select  9990006, 1, 'Y', 'UC_1', 10.12, 'INR'  from dual union
select  9990007, 1, 'Y', 'UC_1', 10.12, 'INR'  from dual union
select  9990008, 1, 'Y', 'UC_1', 10.12, 'INR'  from dual union
select  9990009, 1, 'Y', 'UC_1', 10.12, 'INR'  from dual ;
-- ---------------------------
insert into ecomm_shop.vendor_product_discount (vendor_product_id,vid,is_latest_vid,discount_value,discount_type_code )
select  9990000, 1, 'Y', 10.00, 'DC_PERCENT'  from dual union
select  9990001, 1, 'Y', 10.00, 'DC_PERCENT'  from dual union
select  9990002, 1, 'Y', 10.00, 'DC_PERCENT'  from dual union
select  9990003, 1, 'Y', 10.00, 'DC_PERCENT'  from dual union
select  9990004, 1, 'Y', 10.00, 'DC_PERCENT'  from dual union
select  9990005, 1, 'Y', 10.00, 'DC_PERCENT'  from dual union
select  9990006, 1, 'Y', 10.00, 'DC_PERCENT'  from dual union
select  9990007, 1, 'Y', 10.00, 'DC_PERCENT'  from dual union
select  9990008, 1, 'Y', 10.00, 'DC_PERCENT'  from dual union
select  9990009, 1, 'Y', 10.00, 'DC_PERCENT'  from dual ;
-- ---------------------------
insert into ecomm_shop.vendor_product_image (vendor_product_id,iteration,image_path )
select  9990, 1, '/var/tmp'  from dual union
select  9991, 1, '/var/tmp'  from dual union
select  9992, 1, '/var/tmp'  from dual union
select  9993, 1, '/var/tmp'  from dual union
select  9994, 1, '/var/tmp'  from dual union
select  9995, 1, '/var/tmp'  from dual union
select  9996, 1, '/var/tmp'  from dual union
select  9997, 1, '/var/tmp'  from dual union
select  9998, 1, '/var/tmp'  from dual union
select  9999, 1, '/var/tmp'  from dual ;
