import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


import json
import openai,os
#from langchain.agents import AgentType, initialize_agent, Tool
#from langchain.chat_models import ChatOpenAI

#from langchain.chains import ConversationChain
#from langchain.memory import ConversationBufferMemory , ConversationBufferWindowMemory
#from langchain.chat_models import ChatOpenAI
# from langchain.prompts import (    ChatPromptTemplate,    MessagesPlaceholder,    SystemMessagePromptTemplate,    HumanMessagePromptTemplate)

secret_key=os.environ["OPENAI_API_KEY"]

class DBsearchClass():
#  def __init__(self,template,pkl_tot,pkl_vec):
  def __init__(self,pkl_tot,pkl_vec):
    from functions.function1 import ( stop_watch )
    self.stop_watch = stop_watch()                     # テスト用であり、運用時には不要
    ## 2023-11-07 類似性検索以外は不使用
    self.df_tot,self.df_vec = self.load_DB(pkl_tot,pkl_vec)


  def load_DB(self,pkl_tot,pkl_vec):
    import pickle
    from functions.function4 import read_pkl
    from functions.function0 import ( bprint,fprint )
    if os.path.exists(pkl_tot):
      fprint(pkl_tot,"から読込みます")
      df_tot=read_pkl(pkl_tot)
    else:
      print(pkl_tot,"がありません")
      raise ValueError

    if os.path.exists(pkl_vec):
      fprint(pkl_vec,"から読込みます")
      df_vec=read_pkl(pkl_vec)
    else:
      print(pkl_vec,"がありません")
      raise ValueError

    return df_tot,df_vec

  def get_info(self,usr_msg): ## 2023-11-08
    self.stop_watch.start()
    from functions.function3 import ( retrieveDF2, check_priority,remove_element)
    df_hit=retrieveDF2(self.df_tot,self.df_vec,usr_msg)
    if df_hit is None:
      ret = "NoHits"
    else:
      check_priority(df_hit)                     # 2024-01-04 similarity 優先度 調査用なので、AWSへの実装不要
      df_hit=df_hit.drop(columns=['similarity']) # 2023-11-18 'similarity'を除外
      dic=df_hit.T.to_dict()

      ret=str(list(dic.values())).replace("'all':",'')  # json.dumps(dic,ensure_ascii=False) 2023-11-18　JSONだと、キーをLLMが勘違い
      while len(dic)>0:
        ret=str(list(dic.values())).replace("'all':",'')  # json.dumps(dic,ensure_ascii=False) 2023-11-18　JSONだと、キーをLLMが勘違い
        if len(ret)<10000: break                  # 望ましい文字数　## 2023-12-24 10倍
        dic_old=dic
        remove_element(dic, list(dic.keys())[-1]) # lastの削除
      if len(ret)>=20000:  ret =  'HitTooBig'     # 許容される文字数 以上はToo Big

    self.stop_watch.end_start(ret,'DB_msg=')
    if len(ret)> 50: ret = '参考：'+ret           # 短い返値は正常ではない
    else:            ret = ''
    return ret


