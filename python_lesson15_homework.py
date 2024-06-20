# -*- coding: utf-8 -*-
"""python_lesson15_Homework

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bNX_EhLes9-qxy_2GMEOS8SQa04J5SbQ
"""

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
data.loc[data['whoAmI'] == 'human', 'robot'] = '0'
data.loc[data['whoAmI'] == 'human', 'human'] = '1'
data.loc[data['whoAmI'] == 'robot', 'human'] = '0'
del data['whoAmI']

data.head(n = 20)