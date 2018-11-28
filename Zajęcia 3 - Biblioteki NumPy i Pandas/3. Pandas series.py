import numpy as np
import pandas as pd

mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
pandas_from_list = pd.Series(mylist)
pandas_from_array = pd.Series(myarr)
pandas_from_dict = pd.Series(mydict)
