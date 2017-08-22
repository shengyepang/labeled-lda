# -*- coding: GBK -*-
import MySQLdb
import sys
import re
import progressbar
import nltk
from nltk.stem import PorterStemmer as ps
class Sql_Deal:
    #��Ĺ��캯��������psʵ��������mysql.connectʵ��
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='931011', db='webservice1', charset='utf8mb4')
        self.ps=ps()
        self.bar = progressbar.ProgressBar()
    #�����ͷ�connect����
    def close(self):
        self.conn.close()

    def write_arry(self):
        self.cur=self.conn.cursor()
        Id_Title_Query='(select ID,Name,Description from `apibasic`  limit 12000,2000)'
        Else_Tag_Query='(select CateID from apicate where ApiID=%s and IsPri=0)'
        First_Tag_Query='(select CateID from apicate where ApiID=%s and IsPri=1)'
        self.cur.execute(Id_Title_Query)
        Id_Title = self.cur.fetchall()
        Else_Tag=[]                                             #Else_Tag      [((20090,),(20047,)),()]
        First_Tag=[]                                            #First_Tag     [((20090L,),), ((20015L,),), ((20024L,),), ((20162L,),)]
        Else_Tag_f=[]
        #����һ��������ת��Ϊ�ַ����Ĺ��ܺ����������ַ���
        def arry_to_str(self, arry):
            self.str = ' '.join(map(lambda i: str(i), arry))
            return self.str
        #��apiIDΪ��������ѯ��Ӧ�ĳ���һ��ǩ֮��ı�ǩ
        for i in Id_Title:
            self.cur.execute(Else_Tag_Query,(i[0],))
            Else_Tag.append(self.cur.fetchall())
        #��Else_Tagת��Ϊ[[20142L], [20208L, 20202L, 20206L], [20220L]]����Else_Tag_f��
        for tag in Else_Tag:
            temp=[]
            for i in range(len(tag)):
                temp.append(tag[i][0])
            Else_Tag_f.append(temp)
        #��apiIDΪ��������ѯ��Ӧ�ĳ���һ��ǩ֮��ı�ǩ
        for i in Id_Title:
            self.cur.execute(First_Tag_Query, (i[0],))
            First_Tag.append(self.cur.fetchall())
        Id_Title_f=[]
        #��Id_Titleת��Ϊ[[A,B,C],[A,B,C]]  AΪID,BΪTITLE,CΪDESCRIPTION,�����Id_Title_f��
        for i in Id_Title:
            Id_Title_f.append(list(i))
        for i in self.bar(range(len(Id_Title_f))):
            Id_Title_f[i][1]=Id_Title_f[i][1].lower()                                                         #������Сд
            Id_Title_f[i][2]=Id_Title_f[i][2].lower()                                                         #������Сд
            Id_Title_f[i][2]=re.sub("http:.*? | http:.*|https:.*? |https:.*",'',Id_Title_f[i][2])                             #ɾ�������е���ַ��ַ
            #ɾ������������е�ͣ�÷���
            Id_Title_f[i][1]=Id_Title_f[i][1].replace(',','').replace('.','').replace('[','').replace(']','').replace('(','').replace(')','').replace("'",'').replace('-','').replace(':','').replace('!','').replace('/','')
            Id_Title_f[i][2]=Id_Title_f[i][2].replace(',','').replace('.','').replace('[','').replace(']','').replace('(','').replace(')','').replace("'",'').replace('-','').replace(':','').replace('!','').replace('\n',' ').replace('/','')
            #�������ַ����Կո�ָ�Ϊ���飬ȥ�����еĴ����ֺͿո����п��ܴ����ַ�֮���ж���ո�����
            temp_list_des=filter(lambda i: not i.isdigit() and i != '',Id_Title_f[i][2].split(' '))
            #���������ݽ��д��Ա�ע�����������������
            temp_list_des_f=[]
            tagged_list_des=nltk.pos_tag(temp_list_des)
            #�����Ա�ע��������У�����������Ҫ�Ĵ���
            for j in range(len(tagged_list_des)):
                if (tagged_list_des[j][1]=='NN'or tagged_list_des[j][1]=='NNS'or tagged_list_des[j][1]=='JJ'or tagged_list_des[j][1]=='NNP'or tagged_list_des[j][1]=='NNPS' or tagged_list_des[j][1]=='JJR' or tagged_list_des[j][1]=='JJS' or tagged_list_des[j][1]=='FW'):
                    temp_list_des_f.append(self.ps.stem(temp_list_des[j]))             #stem������ÿ������ȡ�ʸ�
            #������������������ϳ��ַ�������Id_Title_f��
            Id_Title_f[i][2]=' '.join(temp_list_des_f)
            #�Ա�����д��Ա�ע ����ͬ��
            temp_list_title = filter(lambda i: not i.isdigit() and i != '', Id_Title_f[i][1].split(' '))
            temp_list_title_f=[]
            #�Ա������ݽ��д��Ա�ע�����������������
            tagged_list_title = nltk.pos_tag(temp_list_title)
            for j in range(len(tagged_list_title)):
                if (tagged_list_title[j][1] == 'NN' or tagged_list_title[j][1] == 'NNS' or tagged_list_title[j][1] == 'JJ' or tagged_list_title[j][1]=='NNP' or tagged_list_title[j][1]=='NNPS' or tagged_list_title[j][1]=='JJR' or tagged_list_title[j][1]=='JJS' or tagged_list_title[j][1]=='FW'):
                    temp_list_title_f.append(self.ps.stem(temp_list_title[j]))

            Id_Title_f[i][1] = ' '.join(temp_list_title_f)

        Process_Text=[]
        #��������ѵ������
        # for i in range(len(Id_Title_f)):
        #     #����if����������Ԫ�ؽ����пգ���ֹ����Խ�磬������������б��浽����Process_Text��
        #     if len(First_Tag[i])==0 and len(Else_Tag_f[i])==0:
        #         continue
        #     elif len(First_Tag[i])!=0 and len(Else_Tag_f[i])==0:
        #         p=str(Id_Title_f[i][0])+':'+'['+str(First_Tag[i][0][0])+']'+str(Id_Title_f[i][1])+' '+str(Id_Title_f[i][2])
        #         Process_Text.append(p)
        #     elif len(First_Tag[i])==0 and len(Else_Tag_f[i])!=0:
        #         p=str(Id_Title_f[i][0])+':'+'['+arry_to_str(self,Else_Tag_f[i])+']'+str(Id_Title_f[i][1])+' '+str(Id_Title_f[i][2])
        #         Process_Text.append(p)
        #     else:
        #         p=str(Id_Title_f[i][0])+':'+'['+str(First_Tag[i][0][0])+' '+arry_to_str(self,Else_Tag_f[i])+']'+str(Id_Title_f[i][1])+' '+str(Id_Title_f[i][2])
        #         Process_Text.append(p)

        #�����ޱ�ǩ��������
        for i in range(len(Id_Title_f)):
            #����if����������Ԫ�ؽ����пգ���ֹ����Խ�磬������������б��浽����Process_Text��
            if len(First_Tag[i])==0 and len(Else_Tag_f[i])==0:
                continue
            elif len(First_Tag[i])!=0 and len(Else_Tag_f[i])==0:
                p=str(Id_Title_f[i][0])+':'+'['+']'+str(Id_Title_f[i][1])+' '+str(Id_Title_f[i][2])
                Process_Text.append(p)
            elif len(First_Tag[i])==0 and len(Else_Tag_f[i])!=0:
                p=str(Id_Title_f[i][0])+':'+'['+']'+str(Id_Title_f[i][1])+' '+str(Id_Title_f[i][2])
                Process_Text.append(p)
            else:
                p=str(Id_Title_f[i][0])+':'+'['+']'+str(Id_Title_f[i][1])+' '+str(Id_Title_f[i][2])
                Process_Text.append(p)
        #��Process_Text�Ի��з�Ϊ�ָ�д���ļ���
        fp = open('C:/Users/PSY/Desktop/result_test.txt', 'w')
        a_str = '\n'.join(map(lambda i: str(i), Process_Text))
        fp.write(a_str)
        fp.close()
reload(sys)
sys.setdefaultencoding('utf-8')
G=Sql_Deal()
G.write_arry()
# G.close()


