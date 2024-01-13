#UI

def important_notice():
  return
  print(  """
  --- 重要: chatGPT-AP利用に関する注意事項　---
  個人情報の保護: chatGPT-APは個人情報を含む情報の入力を受け付けていません。個人情報や機密情報は絶対に入力しないでください。
  適切な利用:     chatGPT-APは尊重とプロフェッショナリズムをもって利用してください。不適切な言葉やコンテンツの利用は禁止されています。
  制限された知識: chatGPT-APは最新の情報を持っていないかもしれません。重要な意思決定には、常に最新かつ確認済みの情報を利用してください。
  エラーと誤解:   chatGPT-APは時折誤解やエラーを生じる可能性があります。重要な情報は常に他の情報源で確認してください。
  システムの記録: すべての会話は、品質保証とトレーニングの目的で記録される可能性があります。プライバシーに関する疑問や懸念がある場合は、管理者に連絡してください。
  法律と規制の遵守: chatGPT-APの利用は、適用される法律と規制を遵守する必要があります。利用者は自身の責任でシステムを利用するものとします。
  """)

class sinput(): # 冒頭でstring(txt)から入力を受け付ける
  def __init__(self,txt=''):
    self.lines=txt.split('\n')
    self.i=0
    self.n=len(self.lines)
    if txt=='':      self.n=0
  def input(self,txt=''):
    from functions.function0 import ( bprint,fprint )
    if self.i<self.n:
      self.i+=1
      ret=self.lines[self.i-1]
      print(txt+ret)
    else:
      ret=input(txt)
    fprint(txt+ret)
    return ret

class ConnectorClass():
  def __init__(self,txt):
    from functions.function0 import ( bprint,fprint )
    self.count=0
    # !rm log.txt
    important_notice()
    print(f"AI{0}> オホーツクもんべつの『紋太』だもん。よろしくね！飲食街の案内は任せてだもん。") # 2023-12-19
    self.S=sinput(txt)

  def input(self):
    from functions.function0 import beep
    beep()
    self.count+=1
    usr_txt=self.S.input(f"usr{self.count}> ")
    return(usr_txt)

  def output(self,txt):
    from functions.function0 import ( bprint,fprint )
    bprint(f'AI{self.count}> {txt}')
