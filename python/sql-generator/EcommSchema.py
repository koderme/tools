#!/usr/bin/python


import  Table
import  Column
import  SqlStatement

cDmy = Column.Column('dummy', 'any', 'any',  'any', 'any')

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def product_category_code(rowCount):

	t = Table.Table('ecomm_shop', 'product_category_code')
	t.add( Column.Column('product_category_code',   cDmy.DT_STR, 'cat-code-',  '',         cDmy.FMT_4d))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def product_sub_category_code(rowCount):

	t = Table.Table('ecomm_shop', 'product_sub_category_code')
	t.add( Column.Column('product_sub_category_code',   cDmy.DT_STR, 'sub-cat-code-',  '',         cDmy.FMT_4d))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def attribute_key_code(rowCount):

	t = Table.Table('ecomm_shop', 'attribute_key_code')
	t.add( Column.Column('attribute_key_code',   cDmy.DT_STR, 'attr-key-code-',  '',         cDmy.FMT_4d))
	t.add( Column.Column('description',          cDmy.DT_STR, 'attr-desc-',      '',         cDmy.FMT_16d))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def payment_type_code(rowCount):

	rowCount=1
	t = Table.Table('ecomm_shop', 'payment_type_code')
	t.add( Column.Column('payment_type_code',   cDmy.DT_STR, '',  'PTC_CREDIT_CARD',    cDmy.FMT_EMPTY))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def currency_code(rowCount):
	rowCount=1
	t = Table.Table('ecomm_shop', 'currency_code')
	t.add( Column.Column('currency_code',   cDmy.DT_STR, '',  'INR',         cDmy.FMT_EMPTY))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def unit_code(rowCount):

	rowCount=1
	t = Table.Table('ecomm_shop', 'unit_code')
	t.add( Column.Column('unit_code',   cDmy.DT_STR, '',  'UC_1',         cDmy.FMT_EMPTY))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def discount_type_code(rowCount):

	t = Table.Table('ecomm_shop', 'discount_type_code')
	t.add( Column.Column('discount_type_code',   cDmy.DT_STR, '',  'DT_PERCENT',         cDmy.FMT_EMPTY))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def shop_artefact(rowCount):

	rowCount=1
	t = Table.Table('ecomm_shop', 'shop_artefact')
	t.add( Column.Column('artefact_name', cDmy.DT_STR, 'artefact-',    '',         cDmy.FMT_2d))
	t.add( Column.Column('file_path',     cDmy.DT_STR, '',             '/var/tmp/',         cDmy.FMT_EMPTY))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def shop_detail(rowCount):

	rowCount=1
	t = Table.Table('ecomm_shop', 'shop_detail')
	t.add( Column.Column('shop_name',   cDmy.DT_STR, '',    'HealtyOptions Inc',         cDmy.FMT_EMPTY))
	t.add( Column.Column('description', cDmy.DT_STR, '',    'HealtyOptions Inc',         cDmy.FMT_EMPTY))
	t.add( Column.Column('motto',       cDmy.DT_STR, '',    'live healthy...live long',  cDmy.FMT_EMPTY))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
#
#----------------------------------------------------------
def customer(rowCount):
	t = Table.Table('ecomm_shop', 'customer')

	t.add( Column.Column('customer_id', cDmy.DT_NUM, '999',  '',  cDmy.FMT_4d))
	t.add( Column.Column('login_id',    cDmy.DT_STR, 'cust_','',  cDmy.FMT_3d))
	t.add( Column.Column('password',    cDmy.DT_STR, 'pass', '',  cDmy.FMT_3d))

	sql = SqlStatement.SqlStatement(t)

	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
#
#----------------------------------------------------------
def customer_profile(rowCount):
	t = Table.Table('ecomm_shop', 'customer_profile')

	t.add( Column.Column('customer_id',   cDmy.DT_NUM, '999',    '',         cDmy.FMT_4d))
	t.add( Column.Column('dob',           cDmy.DT_AUTO,'',       'CURDATE()',cDmy.FMT_EMPTY))
	t.add( Column.Column('first_name',    cDmy.DT_STR, 'f-',     '',         '{:0>5d}'))
	t.add( Column.Column('gender',        cDmy.DT_STR, '',       'M',        cDmy.FMT_EMPTY))
	t.add( Column.Column('last_name',     cDmy.DT_STR, 'l-',     '',         '{:0>5d}'))
	t.add( Column.Column('middle_name',   cDmy.DT_STR, '',       '',         cDmy.FMT_EMPTY))
	t.add( Column.Column('phone_number',  cDmy.DT_STR, '+91 ',   '',         '{:0>10d}'))
	t.add( Column.Column('phone_verified',cDmy.DT_STR, '',       'N',         cDmy.FMT_EMPTY))

	sql = SqlStatement.SqlStatement(t)

	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
#
#----------------------------------------------------------
def customer_address(rowCount):

	t = Table.Table('ecomm_shop', 'customer_address')

	t.add( Column.Column('customer_address_id',   cDmy.DT_NUM, '999',    '',         cDmy.FMT_4d))
	t.add( Column.Column('customer_id',           cDmy.DT_NUM, '999',    '',         cDmy.FMT_4d))
	t.add( Column.Column('address_type',          cDmy.DT_STR, '',       'R',        cDmy.FMT_EMPTY))
	t.add( Column.Column('apartment_building',    cDmy.DT_STR, 'Apt-',   '',         cDmy.FMT_3d))
	t.add( Column.Column('first_line',            cDmy.DT_STR, '',       ' ',        cDmy.FMT_EMPTY))
	t.add( Column.Column('second_line',           cDmy.DT_STR, '',       ' ',        cDmy.FMT_EMPTY))
	t.add( Column.Column('street',                cDmy.DT_STR, '',       '90 feet rd',cDmy.FMT_EMPTY))
	t.add( Column.Column('city',                  cDmy.DT_STR, 'City-',  '',         cDmy.FMT_3d))
	t.add( Column.Column('state',                 cDmy.DT_STR, '',       'MH',       cDmy.FMT_EMPTY))
	t.add( Column.Column('country',               cDmy.DT_STR, '',       'India',    cDmy.FMT_EMPTY))
	t.add( Column.Column('zip_code',              cDmy.DT_NUM, '400',    '',         cDmy.FMT_3d))

	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
#
#----------------------------------------------------------
def customer_payment_info(rowCount):


	t = Table.Table('ecomm_shop', 'customer_payment_info')
	t.add( Column.Column('customer_payment_info_id',   cDmy.DT_NUM, '999',    '',            cDmy.FMT_4d))
	t.add( Column.Column('customer_id',                cDmy.DT_NUM, '999',    '',            cDmy.FMT_4d))
	t.add( Column.Column('payment_type_code',          cDmy.DT_STR, '',       'credit_card', cDmy.FMT_EMPTY))
	t.add( Column.Column('payment_number',             cDmy.DT_STR, '',       '',            cDmy.FMT_16d))
	t.add( Column.Column('expiry_date_mm_yy',          cDmy.DT_STR, '',       '122020',      cDmy.FMT_EMPTY))

	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def vendor(rowCount):

	t = Table.Table('ecomm_shop', 'vendor')
	t.add( Column.Column('vendor_id',   cDmy.DT_NUM, '999',    '',         cDmy.FMT_4d))
	t.add( Column.Column('vendor_name', cDmy.DT_STR, 'vend-',  '',         cDmy.FMT_4d))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def vendor_detail(rowCount):

	t = Table.Table('ecomm_shop', 'vendor_detail')
	t.add( Column.Column('vendor_id',       cDmy.DT_NUM,   '999',   '',         cDmy.FMT_4d))
	t.add( Column.Column('gst_number',      cDmy.DT_STR,  'GST-',   '',         cDmy.FMT_7d))
	t.add( Column.Column('phone_number1',   cDmy.DT_STR,  '+91 ',   '',         cDmy.FMT_10d))
	t.add( Column.Column('phone_number2',   cDmy.DT_STR,  '+91 ',   '',         cDmy.FMT_10d))
	t.add( Column.Column('phone_number3',   cDmy.DT_STR,  '+91 ',   '',         cDmy.FMT_10d))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def vendor_product(rowCount):

	t = Table.Table('ecomm_shop', 'vendor_product')
	t.add( Column.Column('vendor_product_id',  cDmy.DT_NUM,   '999',   '',         cDmy.FMT_4d))
	t.add( Column.Column('vendor_id',          cDmy.DT_NUM,   '999',   '',         cDmy.FMT_4d))
	t.add( Column.Column('product_id',         cDmy.DT_NUM,   '999',   '',         cDmy.FMT_4d))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def vendor_product_price(rowCount):

	t = Table.Table('ecomm_shop', 'vendor_product_price')
	t.add( Column.Column('vendor_product_id',   cDmy.DT_NUM, '999',    '',         cDmy.FMT_4d))
	t.add( Column.Column('vid',                 cDmy.DT_NUM, '',       '1',        cDmy.FMT_EMPTY))
	t.add( Column.Column('is_latest_vid',       cDmy.DT_STR, '',       'Y',        cDmy.FMT_EMPTY))
	t.add( Column.Column('unit_code',           cDmy.DT_STR, '',       'UC_1',     cDmy.FMT_EMPTY))
	t.add( Column.Column('price',               cDmy.DT_NUM, '',       '10.12',    cDmy.FMT_EMPTY))
	t.add( Column.Column('currency_code',       cDmy.DT_STR, '',       'INR',      cDmy.FMT_EMPTY))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def vendor_product_discount(rowCount):

	t = Table.Table('ecomm_shop', 'vendor_product_discount')
	t.add( Column.Column('vendor_product_id',   cDmy.DT_NUM, '999',    '',         cDmy.FMT_4d))
	t.add( Column.Column('vid',                 cDmy.DT_NUM, '',       '1',        cDmy.FMT_EMPTY))
	t.add( Column.Column('is_latest_vid',       cDmy.DT_STR, '',       'Y',        cDmy.FMT_EMPTY))
	t.add( Column.Column('discount_value',      cDmy.DT_NUM, '',       '10.00',    cDmy.FMT_EMPTY))
	t.add( Column.Column('discount_type_code',  cDmy.DT_STR, '',      'DC_PERCENT', cDmy.FMT_EMPTY))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def vendor_product_image(rowCount):

	t = Table.Table('ecomm_shop', 'vendor_product_image')
	t.add( Column.Column('vendor_product_id',   cDmy.DT_NUM, '999',    '',         cDmy.tbd))
	t.add( Column.Column('iteration',           cDmy.DT_NUM, '',       '1',        cDmy.FMT_EMPTY))
	t.add( Column.Column('image_path',          cDmy.DT_STR, '',       '/var/tmp', cDmy.FMT_EMPTY))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def product(rowCount):

	t = Table.Table('ecomm_shop', 'product')
	t.add( Column.Column('product_id',     cDmy.DT_NUM, '999',       '',         cDmy.FMT_4d))
	t.add( Column.Column('product_code',   cDmy.DT_STR, 'pc-',       '',         cDmy.FMT_3d))
	t.add( Column.Column('description',    cDmy.DT_STR, 'prod-desc-','',         cDmy.FMT_16d))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def product_attribute_kv(rowCount):

	t = Table.Table('ecomm_shop', 'product_attribute_kv')
	t.add( Column.Column('product_id',          cDmy.DT_NUM, '999',    '',          cDmy.FMT_4d))
	t.add( Column.Column('attribute_key_code',  cDmy.DT_STR, 'attr-key-code-',  '', cDmy.FMT_4d))
	t.add( Column.Column('attribute_value',     cDmy.DT_STR, 'attr-val',    '',     cDmy.FMT_4d))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def product_category_rel(rowCount):


	t = Table.Table('ecomm_shop', 'product_category_rel')
	t.add( Column.Column('product_id',      cDmy.DT_NUM,     '999',        '',      cDmy.FMT_4d))
	t.add( Column.Column('iteration',       cDmy.DT_NUM,     '',           '1',     cDmy.FMT_EMPTY))
	t.add( Column.Column('category_code1',  cDmy.DT_STR,     'cat-code-',  '',      cDmy.FMT_4d))
	t.add( Column.Column('category_code2',  cDmy.DT_STR,     'cat-code-',  '',      cDmy.FMT_4d))
	t.add( Column.Column('category_code3',  cDmy.DT_STR,     'cat-code-',  '',      cDmy.FMT_4d))
	t.add( Column.Column('sub_category_code1',  cDmy.DT_STR, 'sub-cat-code-',  '',  cDmy.FMT_4d))
	t.add( Column.Column('sub_category_code2',  cDmy.DT_STR, 'sub-cat-code-',  '',  cDmy.FMT_4d))
	t.add( Column.Column('sub_category_code3',  cDmy.DT_STR, 'sub-cat-code-',  '',  cDmy.FMT_4d))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)


#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def tbd(rowCount):

	t = Table.Table('ecomm_shop', 'tbd')
	t.add( Column.Column('tbd',   cDmy.tbd, '999',    '',         cDmy.tbd))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
# Main
#----------------------------------------------------------
rowCount=10

functions = [
"product_category_code",
"product_sub_category_code",
"attribute_key_code",
"payment_type_code",
"currency_code",
"unit_code",
"discount_type_code",

"shop_artefact",
"shop_detail",


"customer",
"customer_profile",
"customer_address",
"customer_payment_info",

"product",
"product_attribute_kv",
"product_category_rel",

"vendor",
"vendor_detail",
"vendor_product",
"vendor_product_price",
"vendor_product_discount",
"vendor_product_image",


]

functions2 = [
"vendor_product_discount",
]

for f in functions:
	print("-- ---------------------------")
	str = eval(f+'(rowCount)')
	print(str)


