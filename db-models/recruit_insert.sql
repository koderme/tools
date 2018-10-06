-- ---------------------------
insert into recruit.location_mast (location_code,location_description )
select  'loc-code-0000', 'loc-desc-0000000000'  from dual union
select  'loc-code-0001', 'loc-desc-0000000001'  from dual union
select  'loc-code-0002', 'loc-desc-0000000002'  from dual union
select  'loc-code-0003', 'loc-desc-0000000003'  from dual union
select  'loc-code-0004', 'loc-desc-0000000004'  from dual union
select  'loc-code-0005', 'loc-desc-0000000005'  from dual union
select  'loc-code-0006', 'loc-desc-0000000006'  from dual union
select  'loc-code-0007', 'loc-desc-0000000007'  from dual union
select  'loc-code-0008', 'loc-desc-0000000008'  from dual union
select  'loc-code-0009', 'loc-desc-0000000009'  from dual ;
-- ---------------------------
insert into recruit.requirement (requirement_id,requirement_code,client,marketplace,location_code,interview_addr,role,min_ctc,max_ctc,min_exp,max_exp,number_of_positions )
select  9990000, 'req-0000', 'cli-00000', 'qzx', 'chennai', 'addr100000', 'developer', 9990000, 9990000, 9990000, 9990000, 9990000  from dual union
select  9990001, 'req-0001', 'cli-00001', 'qzx', 'chennai', 'addr100001', 'developer', 9990001, 9990001, 9990001, 9990001, 9990001  from dual union
select  9990002, 'req-0002', 'cli-00002', 'qzx', 'chennai', 'addr100002', 'developer', 9990002, 9990002, 9990002, 9990002, 9990002  from dual union
select  9990003, 'req-0003', 'cli-00003', 'qzx', 'chennai', 'addr100003', 'developer', 9990003, 9990003, 9990003, 9990003, 9990003  from dual union
select  9990004, 'req-0004', 'cli-00004', 'qzx', 'chennai', 'addr100004', 'developer', 9990004, 9990004, 9990004, 9990004, 9990004  from dual union
select  9990005, 'req-0005', 'cli-00005', 'qzx', 'chennai', 'addr100005', 'developer', 9990005, 9990005, 9990005, 9990005, 9990005  from dual union
select  9990006, 'req-0006', 'cli-00006', 'qzx', 'chennai', 'addr100006', 'developer', 9990006, 9990006, 9990006, 9990006, 9990006  from dual union
select  9990007, 'req-0007', 'cli-00007', 'qzx', 'chennai', 'addr100007', 'developer', 9990007, 9990007, 9990007, 9990007, 9990007  from dual union
select  9990008, 'req-0008', 'cli-00008', 'qzx', 'chennai', 'addr100008', 'developer', 9990008, 9990008, 9990008, 9990008, 9990008  from dual union
select  9990009, 'req-0009', 'cli-00009', 'qzx', 'chennai', 'addr100009', 'developer', 9990009, 9990009, 9990009, 9990009, 9990009  from dual ;
