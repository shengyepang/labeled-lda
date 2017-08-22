import MySQLdb

conn=MySQLdb.connect(host='localhost', user='root', passwd='931011', db='backup', charset='utf8mb4')
cur=conn.cursor()
# query_select_cateID='select ID from category where Amount<283 '
# cur.execute(query_select_cateID)
# cateID=cur.fetchall()
# print cateID
# cateID_list=[]
# for i in cateID:
#     cateID_list.append(str(i[0]))
# # for i in range(len(cateID_list)):
# #     cateID_list[i]='\''+cateID_list[i]
# str_cateID=','.join(cateID_list)
# str_cateID=str_cateID.replace(',','\',\'')
# print str_cateID
# print isinstance(str_cateID,str)
query_select_apiID='DELECT from apibasic where apibasic.ID in (select distinct ApiID from apicate where CateID in (select CateID.ID from category where Amount<121 ))'
cur.execute(query_select_apiID)
# ApiID=cur.fetchall()
# print len(ApiID)