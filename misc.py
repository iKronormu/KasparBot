import random as rdm

def choose_laugh():
    laughs = [' haha', ' ha!', ' bahaha!', ' hehe']
    laugh = rdm.choice(laughs)
    return str(laugh)