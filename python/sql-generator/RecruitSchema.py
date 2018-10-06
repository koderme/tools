#!/usr/bin/python


import  Table
import  Column
import  SqlStatement

cDmy = Column.Column('dummy', 'any', 'any',  'any', 'any')

#----------------------------------------------------------
# tbd
#----------------------------------------------------------
def location_mast(rowCount):

	t = Table.Table('recruit', 'location_mast')
	t.add( Column.Column('location_code',   cDmy.DT_STR, 'loc-code-',  '',         cDmy.FMT_4d))
	t.add( Column.Column('location_description',   cDmy.DT_STR, 'loc-desc-',  '',         cDmy.FMT_10d))
	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)

#----------------------------------------------------------
#
#----------------------------------------------------------
def requirement(rowCount):


	t = Table.Table('recruit', 'requirement')
	t.add( Column.Column('requirement_id',   cDmy.DT_NUM, '999',  '',        cDmy.FMT_4d))
	t.add( Column.Column('requirement_code', cDmy.DT_STR, 'req-', '',    cDmy.FMT_4d))
	t.add( Column.Column('client',           cDmy.DT_STR, 'cli-', '',    cDmy.FMT_5d))
	t.add( Column.Column('marketplace',      cDmy.DT_STR, '',     'qzx',     cDmy.FMT_EMPTY))
	t.add( Column.Column('location_code',    cDmy.DT_STR, '',     'chennai', cDmy.FMT_EMPTY))
	t.add( Column.Column('interview_addr',   cDmy.DT_STR, 'addr1',   '',        cDmy.FMT_5d))
	t.add( Column.Column('role',             cDmy.DT_STR, '',        'developer',       cDmy.FMT_EMPTY))
	t.add( Column.Column('min_ctc',          cDmy.DT_NUM, '999',     '',        cDmy.FMT_4d))
	t.add( Column.Column('max_ctc',          cDmy.DT_NUM, '999',     '',        cDmy.FMT_4d))
	t.add( Column.Column('min_exp',          cDmy.DT_NUM, '999',     '',        cDmy.FMT_4d))
	t.add( Column.Column('max_exp',          cDmy.DT_NUM, '999',     '',        cDmy.FMT_4d))
	t.add( Column.Column('number_of_positions', cDmy.DT_NUM, '999',  '',        cDmy.FMT_4d))

	sql = SqlStatement.SqlStatement(t)
	return sql.generateInsert() + sql.generateSelect(rowCount)


#----------------------------------------------------------
# Main
#----------------------------------------------------------
rowCount=10

functions = [
"location_mast",
"requirement",
]

for f in functions:
	print("-- ---------------------------")
	str = eval(f+'(rowCount)')
	print(str)


