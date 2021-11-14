#!/usr/bin/env python
# coding: utf-8

# # Basic of an array

# In[1]:


import numpy
my_array = numpy.array([5,6,7,8])
print(my_array)


# # Array Examples

# In[2]:


import numpy as np
a_list = [1,2,3,4]
a_list


# # Example of an array operation

# In[6]:


import numpy as np
array_c = np.array([4,5,6])
array_d = np.array([7,8,9])
print(array_c + array_d)


# # Examples of array indexing

# In[7]:


import numpy as np
weeks_array = np.array(['monday', 'tuesday', 'wednesday', 'thursday'])
print(weeks_array[0])


# # interactive examples of a List to an Array

# In[8]:


import numpy as np
prices=[130,50,98,25,36,426,258,459,554,58,78]
earnings=[8,98,54,89,78,32,12,87,24,85,47,12,30]
prices_array= np.array(prices)
earnings_array=np.array(earnings)
print(prices_array)
print(earnings_array)


# # Add a column

# In[9]:


import numpy
a=numpy.array([[1,2,3],[4,5,6]])
b=numpy.array([[20],[80]])
NewArray=numpy.append(a,b,axis=1)
print(NewArray)


# # Sorting Arrays

# In[10]:


import numpy as np
arr = np.array([6,5,4,3])
print(np.sort(arr))


# # Remove Array Elements

# In[13]:


import numpy as np
#create a numpy array
 arr = np.array([1,2,3,4,5])
#remove element at index 2
 arr_new = np.delete(arr,2)
#display the array
print("Original array:",arr)


# # 1D numpy array
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[14]:


#create 1D numpy from list
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print('1D numpy array:')
print(arr)


# # Reshape 1D array to 2D array or Matrix

# In[15]:


arr = np.array([0,1,2,3,4,5,6,7,8,9])
#converting
arr_2d = np.reshape(arr,(2,5))
print(arr_2d)


# # Reshaped 2D array is a view of 1D array
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




