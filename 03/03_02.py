#%%
import numpy as np
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
sns.set()
%matplotlib inline

%precision 3

from sklearn import linear_model

#%%
import requests, zipfile
from io import StringIO
import io

#%%
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00356/student.zip'

r = requests.get(url, stream=True)

z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

#%%
DATA_PATH = './03/chap3/'
FILE_NAME = 'student-mat.csv'

student_read_math = pd.read_csv(DATA_PATH + FILE_NAME, sep = ';')

#%%
student_read_math.info()

#%%
student_read_math.groupby(['school','sex'])['absences'].mean()


#%%
