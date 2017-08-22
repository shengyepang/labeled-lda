# -*- coding: UTF-8 -*-
import MySQLdb,re,io
conn=MySQLdb.connect(host='localhost', user='root', passwd='931011', db='webservice1', charset='utf8mb4')
cur=conn.cursor()
ApiID_Name_Query='select Name from apibasic where ID=%s'
CatID_Name_Query='select Name from category where ID=%s'
First_Name_Query = 'select PriCateName from new where ID=%s'
Else_Name_Query = 'select SubCateNames from new where ID=%s '

f=open('C:/Users/PSY/workspace/JGibbLabeledLDA/src/resource/docWords.txt.model.theta')
raw=f.readlines()
f.close()
f=open('C:/Users/PSY\Desktop/result.txt_output.txt')
raw_cate=f.readlines()
f.close()
result_txt = []
for i in range(len(raw_cate)):
    raw_cate[i]=raw_cate[i].replace('\n','')
for line in raw:
    a=re.split(' |\n',line)
    Api_ID=int(a[0])
    del a[0]
    a=[float(a) for a in a if a]
    max=0
    for i in range(len(a)-1):
        if a[i+1]>a[max]:
            max=i+1
    First_Tag=max
    First_Tag_ID=raw_cate[First_Tag]
    Else_tag_ID=[]

    Else_tag=[]
    for i in range(len(a)):
        if a[i]>0.008 :
            Else_tag.append(i)
    Else_tag_F=filter(lambda i : i!=max, Else_tag)

    for i in Else_tag_F:
        if i!=None:
            Else_tag_ID.append(long(raw_cate[i]))
    Else_tag_ID=tuple(Else_tag_ID)
    # print Else_tag_ID
    cur.execute(ApiID_Name_Query,(Api_ID,))
    Api_Name=cur.fetchall()

    cur.execute(CatID_Name_Query,(First_Tag_ID,))
    First_Tag_Name=cur.fetchall()

    Else_tag_Name_Temp=[]
    for i in Else_tag_ID:
        cur.execute(CatID_Name_Query,(i,))
        temp=cur.fetchall()
        temp2=[]
        for j in range(len(temp)):
            temp2.append(list(temp[j]))
        Else_tag_Name_Temp.append(temp2[0][0])

    Else_tag_Name=' '.join(Else_tag_Name_Temp)
    cur.execute(First_Name_Query,(Api_ID,))
    Real_First_Name_Temp=cur.fetchall()
    Real_First_Name=str(Real_First_Name_Temp[0][0])
    cur.execute(Else_Name_Query,(Api_ID,))
    Real_Else_Name_Temp=cur.fetchall()
    Real_Else_Name= str(Real_Else_Name_Temp[0][0])

    result_line= 'API_name:'+Api_Name[0][0]+'\n'+'predicted first lable:'+First_Tag_Name[0][0]+'\n'+'real:'+Real_First_Name+'\n'+'predicted else lables:'+Else_tag_Name+'\n'+'real:'+Real_Else_Name+'\n'
    result_txt.append(result_line)
fp = io.open('C:/Users/PSY/Desktop/predict_result.txt', 'w',encoding='utf8')
a_str = '\n'.join(result_txt)
print a_str
fp.write(a_str)
fp.close()
    # print str(First_Tag) + ' ' + Else_tag_F_Print

# for line in raw:
#     a=re.split(' |\n',line)
#     del a[0]
#     a=[float(a) for a in a if a]
#     b=sorted(a)
#     b.reverse()
#     k=3
#     d=[]
#     for i in range(k):
#         c=0
#         while True:
#             if a[c]==b[i]:
#                 d.append(c)
#                 a[c]=0
#                 break
#             else:
#                 c+=1
#     print(d)
'''
    fp=open('C:/Users/PSY/Desktop/deal.txt','a')
    a_str= ' '.join(map(lambda i:str(i),a))
    fp.write(a_str)
    fp.close()
'''

