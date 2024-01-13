# DBファイル

import pickle
def to_pkl(v,pkl_file):
  with open(pkl_file,"wb") as f:    pickle.dump(v, f)

def read_pkl(pkl_file):
  with open(pkl_file, "rb") as f:    v = pickle.load(f)
  return(v)
