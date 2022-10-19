#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import random


def Generate_Dist(mu, sigma, size):


  SIZE_OF_ARRAY = size
  first_dist = np.zeros(SIZE_OF_ARRAY)

  mu_1 = mu
  sigma_1 = sigma

  for i in range(SIZE_OF_ARRAY):
       first_dist[i] = random.normalvariate(mu_1, sigma_1)   
        
  df_first_dist = pd.DataFrame(first_dist, columns = ['Column_A'])
    
  return df_first_dist

