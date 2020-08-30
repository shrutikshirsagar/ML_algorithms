import numpy as np

import pandas as pd

import glob
import os
filelist = [f for f in os.listdir("\\home\\shruti\\Desktop\\try\\")]
print(filelist)
for f in filelist:
    df = pd.read_csv(f,delimiter=';')
    df.drop(df.columns[0],axis=1,inplace=True)
    df.drop(df.columns[0],axis=1,inplace=True)
    df = df.rolling(10).mean() 
    df = df.iloc[::10, :]
    df.to_csv('/home/shruti/Desktop/try/filename.csv', index=True)
   
        
#df.set_index(np.arange(len(df)) // 10).mean()
#df.groupby(np.arange(len(df))//10).mean()
#df.groupby(np.arange(len(df))//10).mean()
#df.set_index(np.arange(len(df)) // 2).mean(level=0)
#df.groupby(np.arange(len(df.index))//2).mean()
#pd.DataFrame(df.values.reshape(-1,2,df.shape[1]).mean(1))

        
#frame = pd.DataFrame()
#list_ = []
#for files in allFiles:
#    df = pd.read_csv(files,delimiter=';')
 #   df.drop(df.columns[0],axis=1,inplace=True)
  #  df.drop(df.columns[0],axis=1,inplace=True)
   # df = df.rolling(10).mean() 
   # df = df.iloc[::10, :]
#df.set_index(np.arange(len(df)) // 10).mean()
#df.groupby(np.arange(len(df))//10).mean()
#df.groupby(np.arange(len(df))//10).mean()
#df.set_index(np.arange(len(df)) // 2).mean(level=0)
#df.groupby(np.arange(len(df.index))//2).mean()
#pd.DataFrame(df.values.reshape(-1,2,df.shape[1]).mean(1))

    #df.to_csv('/home/shruti/Desktop/try/files.csv', index=True)filelist = [f for f in os.listdir('/home/shruti/Desktop/try')]


