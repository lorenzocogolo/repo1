#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import* 


# In[2]:


def cheaters_data():
    """Reads the file cheaters.txt and returns the data as a list of lists."""
    
    data = []
    for line in open('../assignment-final-data/cheaters.txt', 'r').readlines():
        cheaters_list = [k.strip() for k in line.split('\t')]
        data.append(cheaters_list)
    
    for i in range(len(data)):
        data[i][1] = datetime.strptime(data[i][1], '%Y-%m-%d')
        data[i][2] = datetime.strptime(data[i][2], '%Y-%m-%d')
    
    return data

cheaters = cheaters_data()


# In[4]:


def kills_data():
    """Reads the file kills.txt and returns the data as a list of lists."""
    
    data = []
    for line in open('../assignment-final-data/kills.txt', 'r').readlines()[:10000]:
        kills_list = [k.strip() for k in line.split('\t')]
        data.append(kills_list)
        
    for i in range(len(data)):
        data[i][3] = datetime.strptime(data[i][3], '%Y-%m-%d %H:%M:%S.%f')  
    
    return data

kills = kills_data()


# In[5]:


def kills_dic():
    """Gets the kills_data output as input. Produces a dictionary with the unique games, kills and times associated"""
    match = sorted(set([i[0] for i in kills]))

    match_dic = {i: [] for i in match}
    
    for i in match_dic:
        for j in kills:
            if j[0] == i:
                match_dic[i].append(j[1:4])

    return match_dic

dic_kills = kills_dic()

