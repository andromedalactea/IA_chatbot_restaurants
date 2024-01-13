import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


import json
import openai,os
#from langchain.agents import AgentType, initialize_agent, Tool
from langchain.chat_models import ChatOpenAI

from langchain.chains import ConversationChain
#from langchain.memory import ConversationBufferMemory , ConversationBufferWindowMemory
from langchain.memory import ConversationBufferWindowMemory
#from langchain.chat_models import ChatOpenAI
from langchain.prompts import (    ChatPromptTemplate,    MessagesPlaceholder,    SystemMessagePromptTemplate,    HumanMessagePromptTemplate)

secret_key=os.environ["OPENAI_API_KEY"]

class AnsBotClass():
  def __init__(self,language_type,model_name="gpt-4-1106-preview"):
#  def __init__(self,template,model_name="gpt-4-1106-preview"):
    from functions.function1 import ( stop_watch )
    self.stop_watch = stop_watch()                     # テスト用であり、運用時には不要
    from functions.function5 import ( system_prompt )
    if language_type=='zh-cn': template=system_prompt('中国語','请用中文。','中国語以外は使わないでください。')
    elif language_type=='en':  template=system_prompt('英語','','英語以外は使わないでください。')
    else:                      template=system_prompt('','','')
    llm = ChatOpenAI(model_name=model_name, openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.8)
    memory = ConversationBufferWindowMemory(k=5, return_messages=True)    # ConversationBufferMemory(return_messages=True)　k=5で良いか？
    prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(template),
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate.from_template("{input}")
    ])
    self.chain = ConversationChain(memory=memory, prompt=prompt, llm=llm)

  def response(self,input):
    self.stop_watch.start()
    ret = self.chain.predict(input=input)
    self.stop_watch.end_start(ret,'AI_msg=')
    return ret



