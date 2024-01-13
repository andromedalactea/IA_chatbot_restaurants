import numpy as np
import pandas as pd
def cos_similarity(vec1,vec2):
  vec1=np.array(vec1)
  vec2=np.array(vec2)
  return np.dot(vec1,vec2)/np.sqrt(np.dot(vec1,vec1)*np.dot(vec2,vec2))

def cal_similarity(df_vec,query_txt,rows=None,cols=None):
  from langchain.embeddings.openai import OpenAIEmbeddings
  embeddings = OpenAIEmbeddings()
  if rows == None:  rows = [True for a in df_vec.index]
  if cols == None:  cols = list(df_vec.columns.values)
  sim_vec = [-999 for a in rows]
  col_vec = [-999 for a in rows]
  vec1=np.array( embeddings.embed_query(str(query_txt)))
  smax,idx_max,col_max=-999,-999,-999
  for i,idx in enumerate(df_vec.index):
    if not rows[i]:continue
    for j,col in enumerate(cols):
      vec2 = df_vec.loc[idx,col]
      if vec2 == 'nan': continue
      if not isinstance(vec2,list): continue # 2023-11-19 debug
      s=cos_similarity(vec1,vec2)
      if sim_vec[i]<s:
        sim_vec[i]=s
        col_vec[i]=col
        if smax < sim_vec[i]:
          smax=sim_vec[i]
          idx_max,col_max=idx,col
  return sim_vec,smax,idx_max,col_max,col_vec

def get_similarity3(df_tot,df_vec,query_txt,rows): ## 2024-01-03  query_txtに格納されたvectorとdf_vecとの類似性を計算し、best を返す
  EPS=0.02
  sim_vec,smax,idx_max,col_max,col_vec = cal_similarity(df_vec,query_txt,rows=rows)
  if smax<0: return None
  df_sim = pd.DataFrame({'similarity':sim_vec},index=df_vec.index)
  df_sim['similarity']+=df_tot['all'].str.contains('高')*EPS*2 + df_tot['all'].str.contains('中')*EPS    ## 2024-01-03
  return df_sim.sort_values('similarity', ascending=False).head(10)                                      ## 2023-12-25 head(5) 5個に絞っている


def retrieveDF2(df_tot,df_vec,query_txt): ## 2023-11-08 # def retrieveDF(df_tot,df_vec,query_tuples): # RAG本体
  rows= [True for a in df_vec.index]                           ## 全て検索対象
  df_sim=get_similarity3(df_tot,df_vec,query_txt,rows)         ## 2024-01-03   df_sim=get_similarity2(df_vec,query_txt,rows)
  return pd.concat([df_sim,df_tot['all']],axis=1,join='inner') ##必要行のみ、allをつけて返す

def remove_element(dictionary, key):
    if key in dictionary:
        value = dictionary.pop(key)
        return value
    else:
        raise KeyError(f'Key "{key}" not found in dictionary')

def check_priority(df): # 2024-01-04
    from functions.function0 import ( bprint,fprint )
    EPS=0.01 # 0.02 # 0.03
    h1,h2,m1,m2,l1,l2=9,0,9,0,9,0

    for idx in df.index:
      s=df.loc[idx,'similarity']
      lines=df.loc[idx,'all']
      for line in lines.split('\n'):
        if '店名：' in line: name=line
        if '優先度：' in line: priority=line
        if 'ジャンル：' in line: genre=line
      fprint(s,priority,genre,name)

      if '優先度：高'in line:
        if h1> s:h1=s
        if h2< s:h2=s
      if '優先度：中' in line:
        if m1> s:m1=s
        if m2< s:m2=s
      if '優先度：低' in line:
        if l1> s:l1=s
        if l2< s:l2=s

    l1-=EPS
    l2-=EPS
    h1+=EPS
    h2+=EPS
    fprint(l1,l2,'<',m1,m2,'<',h1,h2)


