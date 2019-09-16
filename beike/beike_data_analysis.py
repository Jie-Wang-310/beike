'''项目名称：贝壳找房杭州二手房数据分析'''
'''作者：@Jack'''


import pandas as pd
import random
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文
plt.rcParams['axes.unicode_minus'] = False   # 用于正常显示负号

# data = pd.read_csv('beike.csv')
# print(data)
#
'''重复值处理'''
# dada_noduplicates = data.drop_duplicates()
# print(dada_noduplicates)

'''空值过滤'''
# data_nonull = dada_noduplicates.dropna()
# print(data_nonull)

'''区域值处理'''
# data_location = data_nonull['title']
# print(data_location)
# data_location.to_csv('data_location.txt',encoding='utf-8')
# f = open('data_location.txt','r',encoding='utf-8')
# w = open('dada_location_cleaned.csv','w',encoding='utf-8')

# lines = f.readlines()
# keywords = [u'西湖',u'钱塘新区',u'下城',u'江干',u'拱墅',u'上城',u'滨江',
#             u'余杭',u'萧山',u'桐庐',u'淳安',u'建德',u'富阳',u'临安']
#
# # keyword = random.choice(keywords)
# for keyword in keywords:
#     for line in lines:
#         if keyword in line:
#             # print(keyword)
#             w.write(keyword+'\n')

# data_location = pd.read_csv('data_location_cleaned.csv',names=['location'])

'''关注量数据处理'''

# data_followInfo = data_nonull['followInfo']
# data_followInfo = data_followInfo.str.split(u'人',expand=True)[0]
# print(data_followInfo)
# data_followInfo.to_csv('data_follow.csv',encoding='utf-8',index=False)
# data_followInfo = pd.read_csv('data_follow.csv',names=['followInfo'])

'''均价和总价,小区名提取'''
# data_avg_total_price = data_nonull[['avg_price','total_price']]
# print(data_avg_total_price)
#
# data_all = data_avg_total_price.join(data_followInfo)
# data_all = data_all.join(data_location)
# print(data_all)
#
# data_followInfo = data_all['followInfo'].fillna(0)
# data_location = data_all['location'].fillna(u'临安')
# data_all = data_avg_total_price.join(data_location)
# data_all_cleaned = data_all.join(data_followInfo)
# print(data_all_cleaned)
# data_all_cleaned.to_csv('data_all_cleaned.csv',encoding='utf-8')

'''数据分析与可视化'''


#分析哪个地区房源平均单价最高？画出可视化图

# data = pd.read_csv('data_all_cleaned.csv')
# print(data)
# data_la = data[['location','avg_price']]
# print(type(data_la))
# print(data_la)
#
# data_typela = data_la.groupby(['location'])['avg_price'].mean()
# print(type(data_typela))
# print(data_typela)
# #
# data_l = data_typela.index
# data_l = list(data_l)
# data_a_mean = data_typela.values
# print(data_a_mean)
# plt.title(u"各地区房源平均单价")
# pic_output = 'avg_price'
#
# for x,y in enumerate(data_a_mean):
#     plt.text(x,y+500,"%.2f" %y,ha='center',va='bottom')   # %.2f表示显示小数点后两位
# bar = plt.bar(data_l,data_a_mean,width=0.5,color='b')
# bar[0].set_color('g')
# bar[-2].set_color('g')
# bar[1].set_color('g')
#
# plt.savefig(u'%s.png' %(pic_output),dpi=500)

# 分析杭州房源平均单价是多少和平均售价是多少？画出可视化图
# data = pd.read_csv('data_all_cleaned.csv')
# data_at = data[['avg_price','total_price']]
#
# avg_price_mean = data['avg_price'].mean()
# total_price_mean = data['total_price'].mean()
# print(avg_price_mean)
# print(total_price_mean)


# 分析杭州房源最多的地方
# data = pd.read_csv('data_all_cleaned.csv')
# print(data)
# data_type_location = data.groupby(['location']).size()
# print(data_type_location)
#
# data_l = data_type_location.index
# data_l = list(data_l)
#
# data_l_sum = data_type_location.values
#
# plt.bar(data_l,data_l_sum,width=0.5,color='b')
# plt.title(u'各个地区房源数量分布情况')
#
# for x,y in enumerate(data_l_sum):
#     plt.text(x,y+20,"%.2f" %y,ha='center',va='bottom')
#
# pic_output = 'location'
# plt.savefig(u'%s.png' %(pic_output))


# 分析杭州关注度最高的地区
data = pd.read_csv('data_all_cleaned.csv')

data_lf = data.groupby(['location'])['followInfo'].sum()
print(data_lf)

data_l = data_lf.index
data_f = data_lf.values

bar = plt.bar(data_l,data_f,width=0.5,color='b')
for x,y in enumerate(data_f):
    plt.text(x,y+20,"%s" %y,ha='center',va='bottom')
bar[3].set_color('g')
bar[-2].set_color('g')
bar[-4].set_color('g')
plt.title(u'各个地区房源关注度')
pic_output = 'followInfo'
plt.savefig(u'%s.png' %(pic_output))

# 分析杭州最贵的房子和最便宜的房子

# data = pd.read_csv('data_all_cleaned.csv')
# data_avg_max = data['avg_price'].max()
# data_avg_min = data['avg_price'].min()
# print(data_avg_max)
# print(data_avg_min)
#
# data_total_max = data['total_price'].max()
# data_total_min = data['total_price'].min()
# print(data_total_max)
# print(data_total_min)
#





plt.style.use('ggplot')
plt.tight_layout()
plt.show()




















































