# 開発時に便利

def beep(sw=1):
  from google.colab import output
  if sw==0: output.eval_js('new Audio("https://upload.wikimedia.org/wikipedia/commons/0/05/Beep-09.ogg").play()')
  else:     output.eval_js('new Audio("https://freesound.org/data/previews/80/80921_1022651-lq.mp3").play()')


def bprint(*args):
  print(*args)
  fprint(*args)

def fprint(*args):
    with open('log.txt', 'a') as fp:
      for a in args:
        fp.write(f'{a} ')
      fp.write('\n')
