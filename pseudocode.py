#edit from gibhub
# coding: utf-8

# In[1]:

#import libraries
#import data
#calculate proportions
#save them as new columns in existing dataframe
#make nice plot of GC content vs. gene content
#save figure to appropriate file


# In[7]:

import pandas
import matplotlib.pyplot as plt

#to make program to run other files
import sys
filename= sys.argv[1]

#%matplotlib inline

human_chr21 = pandas.read_csv(filename, sep='\t')
human_chr21['gc_content']= human_chr21['gc_bases']/ (human_chr21['win_end']- human_chr21['win_start'])
human_chr21['gene_content'] = human_chr21['exon_bases'] / (human_chr21['win_end'] - human_chr21['win_start'])
plt.plot(human_chr21['gene_content'], human_chr21['gc_content'], 'o')
plt.xlabel('Gene Content')
plt.ylabel('GC Content')
plot_file_name=filename+'.plot.png'
plt.savefig(plot_file_name)


# In[3]:




# In[4]:




# In[5]:




# In[ ]:




# In[ ]:



