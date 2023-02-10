#!/usr/bin/env python
# coding: utf-8

# In[9]:


# guess the animal name game
secret_animal = "Jaguar"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_animal and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter your guess")
        guess_count += 1
    else:
        out_of_guesses = True 
if out_of_guesses == True:
    print ("better luck next time")
else:
    print("hurray !! you win")


# In[ ]:





# In[ ]:




