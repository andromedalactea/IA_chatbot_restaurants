def main(txt): # 2023-12-19
  from functions.function6 import    AnsBotClass
  from functions.function7 import  DBsearchClass
  from functions.function8 import  LangJudgeClass
  from functions.function9 import  ConnectorClass
  ""
  from functions.AnsBot import    AnsBotClass
  from functions.DBsearch import  DBsearchClass
  from functions.LangJudge import  LangJudgeClass
  from functions.Connector import  ConnectorClass
  """

  !rm log.txt
  PKL_TOT='functions/tot_monbetsu31.pkl' # 2023-01-02
  PKL_VEC='functions/vec_monbetsu31.pkl'
  DBsearch = DBsearchClass(PKL_TOT, PKL_VEC)
  Connector = ConnectorClass(txt)
  LangJudge=LangJudgeClass()
  candidatetxt, answer='',''

  for count in range(1,15):
    usr_txt=Connector.input()
    if(len(usr_txt)<=0): break
    candidate_txt = DBsearch.get_info(usr_txt + ' '+answer) # 2023-11-20 +answer
    language_type=LangJudge(usr_txt)
    if language_type!='': AnsBot   = AnsBotClass(language_type,model_name="gpt-4-1106-preview")
    answer = AnsBot.response(input='問合せ：'+ usr_txt+candidate_txt)
    Connector.output(answer)
    """
