from step1 import suspects, start_cheating
from step2 import histogram

# compute new suspect lists for each random dictionary in the histogram list
rnd_suspects = [suspects(i) for i in histogram]


# compute new cheaters for each suspect list corresponding to the random dictionaries in the histogram list  
rnd_new_cheaters = [start_cheating(i) for i in rnd_suspects]     
   

