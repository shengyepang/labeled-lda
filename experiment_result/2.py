# import time
# start =time.clock()
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum )
# end = time.clock()
# print('Running time: %s Seconds'%(end-start))

from nltk.stem import PorterStemmer as ps
print ps().stem('eCommerce')