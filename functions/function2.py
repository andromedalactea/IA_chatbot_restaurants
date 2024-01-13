def index_of2(txt,subs):
  ret=99999
  if isinstance(txt,list):
    for sub in subs:
      if txt.count(sub)>0:
        r=txt.index(sub)
        if ret>r: ret=r
  elif isinstance(txt,str):
    sub=subs
    if txt.count(sub)>0:
      r=txt.index(sub)
      if ret>r: ret=r
  if ret>999: return -99
  return ret

def index_of(txt,sub):
  if txt.count(sub)<=0: return -99
  return txt.index(sub)
