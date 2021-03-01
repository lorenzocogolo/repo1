#!/usr/bin/env python
# coding: utf-8

# In[5]:


from datetime import *
from dataread import cheaters,kills,dic_kills


# In[2]:
def cheaters_accounts():
    '''This function takes the cheaters list as input and estrapolates the cheaters' accounts for each match in the dictionary
    It returns a list made of sublists that contain the active cheaters present in each game''' 
    
    match_cheaters = []
    
    for key in dic_kills:
        
        lst = []
        for value in dic_kills[key]:
            
            for i in range(len(cheaters)):            
                if cheaters[i][0] == value[0] and cheaters[i][1] < value[2] < cheaters[i][2]:
                    lst.append(value[0])
            
        unique = sorted(set(lst))
        match_cheaters.append(unique)
        
    return match_cheaters

match_cheaters = cheaters_accounts()



# In[4]:

def suspects(dic):
    '''This function iterates over each game played and firstly: compares each killer to the cheaters list and appends
    the killed player to the suspect list if they are killed by a cheater. Secondly, if this number of kills by a 
    cheater in a game reaches 3, it adds the following killed players to the suspect list.
    It returns the suspect list.'''
    susp_list = []
    loc = 0
    for key in dic:
        
        lst1 = []
        if len(match_cheaters[loc]) > 0: 
            for cheater in cheaters:
                
                count = 0
                for v in dic[key]:
                    if cheater[0] == v[0] and cheater[1] < v[2] < cheater[2]:
                        count += 1
                        lst = []
                        lst.extend([v[1],v[2]])
                        susp_list.append(lst)

#                  for each vlaue[1], if count is >= 3, checks if the account is already in the susp_list 
#                  to avoid duplicates. If this is not the case, add killed player encountered to the suspect list
                    elif count >= 3 and not any(v[1] in sl for sl in susp_list):
                        lst1 = []
                        lst1.extend([v[1],v[2]])
                        susp_list.append(lst1) 
        loc += 1
    return susp_list

susp_list = suspects(dic_kills)


def start_cheating(s_list):
    '''This function iterates over the suspect list and compares each player to the cheaters' accounts.
    If one player is matched to a cheater's account and the cheating start date is less than 5 days from the 
    time when the player was added to the suspect list, the count for the number of players that 
    started cheating is increased. The function returns the number of players that started cheating.'''
    
    count = 0
    for i in s_list:
        for j in cheaters:
            delta = j[1] - i[1]
            
#           compare each suspect to the cheaters list and thier suspect date with the cheating period
            if i[0] == j[0] and delta.days < 5 and delta.days >= 0:
                count += 1
                
    return count

new_cheaters = start_cheating(susp_list)

