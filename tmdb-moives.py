
# coding: utf-8

# # 项目：TMDB电影数据分析
# 
# ## 目录
# <ul>
# <li><a href="#intro">简介</a></li>
# <li><a href="#wrangling">数据整理</a></li>
# <li><a href="#eda">探索性数据分析</a></li>
# <li><a href="#conclusions">结论</a></li>
# </ul>
# 
# <a id='intro'></a>
# ## 简介
# 
# > **提示**：本报告对电影的评分和票房的影响因素（电影类型、预算，导演和演员）进行分析，并可视化结果。

# In[1]:


#   导入语句。
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# <a id='wrangling'></a>
# ## 数据整理
# ### 常规属性

# In[2]:


# 加载数据并打印几行
df = pd.read_csv('tmdb-movies.csv')
df.head(2)


# In[3]:


#   类型，以及是否有缺失数据或错误数据的情况
df.info()


# ### 数据清理（清理列标签，丢空，去重。）

# In[4]:


# 清理无关列标签，检查数据
df = df.drop(['imdb_id', 'budget', 'revenue', 'original_title','homepage','tagline','keywords','overview','runtime','production_companies','release_date','vote_count','release_year'], axis=1)
df.head(3)


# In[5]:


df.shape


# In[6]:


# 丢空、去重，查检数据
df = df.dropna().drop_duplicates()
df.info()


# <a id='eda'></a>
# ## 探索性数据分析
# ### # 电影类型、预算，导演和演员对电影评分的影响？

# In[7]:


# 不少数据列（假定x）包含由竖线字符（|）分隔的多个数值，考虑创建一个新的DataFrame，包含无字符（|）的x列,和相对应的y列
# 生成新DataFrame后，按照新DataFrame的x旳值分组，计算y平均值，排序取最大的前z个，画出直方图
def p(x,y,z):
# 创建“x”数据列元素列表
    list1 = []
    for i in range(10731):
        list1 += df[x].iloc[i].split('|')
# 创建“x”数据列元素索引列表
    idx1 = range(len(list1))
# 创建“y”数据列元素元素列表
    list2 = []
    for j in range(10731):
        for k in range(len(df[x].iloc[j].split('|'))):
            list2.append(df[y].iloc[j])
# 创建一个新的DataFrame包含列x，y
    items = {x : pd.Series(data = list1, index = idx1),
         y : pd.Series(data = list2, index = idx1)}
    df_x_y = pd.DataFrame(items)
# 按照x分组，求y平均值，降序排列，取前z个，画出直方图,
    df_x_y.groupby(x)[y].mean().sort_values(ascending=False).head(z).plot(kind='bar',figsize=(9,4))
    plt.title('The top ' + str(z) + ' '+ x + ' of ' + y)
    plt.xlabel(x)
    plt.ylabel(y);
    


# In[8]:


# 电影类型评分排名（总共有20种电影类型）
p('genres','vote_average',20)


# **结论1：纪录片评分最高，恐怖片评分最低**

# In[9]:


pd.plotting.scatter_matrix(df,figsize=(11,11));


# In[10]:


df.corr()


# **结论2：预算与电影评分关联很小，预算与电影票房关联较大，电影评分与电影票房关联小**

# In[11]:


p('director','vote_average',30)


# **结论3：导演对电影评分影响不明显**

# In[12]:


p('cast','vote_average',30)


# **结论4：演员对电影评分影响也不明显**

# ### 电影类型、预算，导演和演员对票房的影响？

# In[13]:


p('genres','revenue_adj',20)


# ** 结论5：冒险片票房最高，电视电影票房最低，电影类型对票房影响蛮大的**

# In[14]:


p('director','revenue_adj',30)


# **结论6：导演对票房影响蛮大，hamilton luske和clyde geronimi影响力比较突出**

# In[15]:


p('cast','revenue_adj',30)


# ** 结论7：演员对票房影响蛮大**

# <a id='conclusions'></a>
# ## 结论
# 
# **1：纪录片评分最高，恐怖片评分最低；**
# **2：预算与电影评分关联很小，预算与电影票房关联较大，电影评分与电影票房关联小；**
# **3：导演对电影评分影响不明显；**
# **4：演员对电影评分影响也不明显；**
# **5：冒险片票房最高，电视电影票房最低，电影类型对票房影响蛮大的；**
# **6：导演对票房影响蛮大，其中hamilton luske和clyde geronimi影响力比较突出；**
# **7：演员对票房影响蛮大；**
# **局限：票房列存在较多值是0，没有什么好的办法处理。***

# In[16]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

