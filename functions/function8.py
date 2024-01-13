from langdetect import detect
def which_lang(txt,lang0):  # 2023-12-28
  if lang0 !='':
    if   '日本語で' in txt:                      lang='ja'
    elif '英語で' in txt or 'English'    in txt: lang='en'
    elif '中国語で' in txt or '请用中文' in txt: lang='zh-cn'
    else:                                         lang=lang0
  else:
    lang=detect(txt)
    if lang in ['zh-cn','ko']:  lang='zh-cn'
    elif lang in ['en']:          lang='en'
    else:                           lang='ja'
  return lang

class LangJudgeClass():
  def __init__(self):
    self.type_old=''
  def __call__(self,usr_txt):
#    from functions.function5 import which_lang
    from functions.function0 import ( bprint,fprint )
    type_old=self.type_old
    type=which_lang(usr_txt,type_old)
    self.type_old=type
    if type_old==type:       return ''  # 同じならヌル文字を返す
    fprint('言語：',type)       # 2023-12-26
    return type