#!/usr/bin/env python
# coding: utf-8

# In[27]:


import random

adjectives = ["glorious", "shivering","cold","mangled","wretched", "simmering", "sharp", "raging", "deadly"]
nouns = ["rat","human","dinosaur","evil one", "eye", "tentacle", "hole","axe blade", "knife", "heart", "teeth"]
verbs = ["kill", "destroy", "maim", "drink", "feast upon", "drain", "stab", "cut"]
articles = ["a", "an", "the"]
prepositions = ["with", "above", "on", "near", "below", "of"]
adverbs = ["loudly", "quitely",]

def gen_adj():
    print (random.choice(adjectives))

def gen_noun():
    print (random.choice(nouns))

def gen_verb():
    print(random.choice(verbs))
    
def gen_art():
    print(random.choice(articles))
    
def gen_prep():
    print(random.choice(prepositions))
    
def gen_adv():
    print(random.choice(adverbs))


gen_art()
gen_adj()
gen_noun()
gen_prep()
gen_art()
gen_adj()
gen_noun()


# In[28]:


gen_art()


# In[66]:


def gen_line1():
    print("You must overcome the ")
    gen_adj()
    gen_noun()
    


# In[67]:


gen_line1()


# In[71]:


def gen_line2():
    print("before the ")
    gen_noun()
    gen_verb()
    print ("you")


# In[77]:


gen_line1()
gen_line2()


# In[ ]:





# In[ ]:




