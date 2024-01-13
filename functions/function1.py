from datetime import datetime
import time
class stop_watch():
  def __init__(self): self.start()
  def start(self):    self.time0 = datetime.now().timestamp()
  def end(self,txt):
    from functions.function0 import ( bprint,fprint )
    time1 = datetime.now().timestamp() - self.time0
    fprint("{2:5.2f} = {1:d}文字 / {0:5.2f}sec ".format(time1,len(txt),len(txt)/time1))
  def end_start(self,txt,comment=[]):
    from functions.function0 import ( bprint,fprint )
    self.end(txt)
    self.start()
    if len(comment)>1: fprint(comment+txt)
