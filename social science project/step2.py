#!/usr/bin/env python
# coding: utf-8

# In[1]:

from datetime import *
from dataread import *
from step1 import dic_kills,match_cheaters


import random
from copy import deepcopy

def randomisation():
    '''This function creates a new random dictionary from the original dictionary. It then randomly substitutes killers 
    and killed players using the random indexes generated. Games IDs, killing times and cheaters' kills positions are not
    changed. The algorithm is repeted 10 times before the final random dictionary and a 'histogram' list representing
    the random dictionary at each iteration are given as output'''
    
#   initialise random dictionary and histogram list
    random_dic = kills_dic()
    histogram = []
    n = 0
    
#   repeat the randomisation process 10 times
    while n < 10:
        c = 0
        for key in random_dic:
            
            killed_list = []
            
    #       randomise only if there is a cheater inside!
            if len(match_cheaters[c]) > 0:
                for pos in range(len(random_dic[key])):

    #               generate two random indexes to conduct the randomisation
                    loc = random.randint(0,len(random_dic[key]) - 1)
                    loc2 = random.randint(0,len(random_dic[key]) - 1)

    #               if the current killer is not a cheater, and the random killer is not a cheater, swap the current killer 
    #               and killed players with two others within the game using the random indexes and makes sure the killer doesn't kill himself
    #               and the killer hasn't been killed before
                    if random_dic[key][pos][0] not in match_cheaters[c] and random_dic[key][loc][0] !=  random_dic[key][loc2][1] \
                    and random_dic[key][loc][0] not in match_cheaters[c] and random_dic[key][pos][0] not in killed_list \
                    and random_dic[key][loc][0] not in killed_list and random_dic[key][pos][0] not in killed_list:
            
                        random_dic[key][pos][0], random_dic[key][loc][0] = random_dic[key][loc][0], random_dic[key][pos][0]
                        random_dic[key][pos][1], random_dic[key][loc2][1] = random_dic[key][loc2][1], random_dic[key][pos][1]
                        killed_list.append(random_dic[key][pos][1])

    #               if the current killer is a cheater, swap the current killed player only  
                    elif random_dic[key][loc][0] !=  random_dic[key][loc2][1] and random_dic[key][loc][0] not in match_cheaters[c] \
                    and random_dic[key][pos][0] not in killed_list and random_dic[key][loc][0] not in killed_list and random_dic[key][pos][0] not in killed_list:
            
                        random_dic[key][pos][1], random_dic[key][loc2][1] = random_dic[key][loc2][1], random_dic[key][pos][1]
                        killed_list.append(random_dic[key][pos][1])

            c += 1

        histogram.append(deepcopy(random_dic))
        n += 1
        
    return random_dic, histogram
            
random_dic, histogram = randomisation()