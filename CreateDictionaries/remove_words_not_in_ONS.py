
# coding: utf-8
"""
Created on Tue Mar 28 09:38:19 2017

@author: 327660
"""


import pickle
import os
import json
import collections

directory = r"C:\Users\327660\Documents\Job_title_matching"
directory.replace('\\','/')
directory = os.path.normpath(directory)
os.chdir(directory)

#%% Create dictionary of words that exist in ONS classification

# Load dictionary of titles, but no descriptions
with open('titles_mg_ons_nodesc.pkl', 'r') as infile:
    titles_mg_nodesc = pickle.load(infile)

# Get known titles from the dictionary
known_words = []
for key in titles_mg_nodesc.keys():
    for title in titles_mg_nodesc[key]:
        known_words.append(title)

# Generate a Counter object of known words
known_words_list = [item.split() for item in known_words]
known_words_flat = [item for sublist in known_words_list for item in sublist]
known_words_counts = collections.Counter(known_words_flat)

known_words_dict ={}
for key in known_words_counts.keys():
    known_words_dict[key] = known_words_counts[key]
    
# Delete uninformative words that happen to exist in ONS classification
words_to_remove = ['mini', 'x', 'london','nh', 'apprentice', 'graduate', 
                   'for', 'in', 'at', 'senior', 'junior', 'trainee' ]
for word in words_to_remove:
    known_words_dict.pop(word, None)

#%% Write dictionary to pickle and json

pickle.dump(known_words_dict, open('known_words_dict.pkl', 'wb'))

with open('known_words_dict.json', 'w') as fp:
    json.dump(known_words_dict, fp, indent = 4)
    