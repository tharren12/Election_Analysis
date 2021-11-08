import collections
from typing import OrderedDict


print ("Hello World!")

counties = ["Arapahoe","Denver","Jefferson"]

counties[2]

print(counties[-2])

len(counties)

counties[:2]

counties.remove("El Paso")

counties.insert(2, "El Paso")

counties

counties.pop(3)

counties[2] = "El Paso"

counties_tuple = ("Arapahoe","Denver","Jefferson")

len(counties_tuple)

counties_tuple[1:2]

my_dictionary = {}
dict()
my_dictionary = dict()

counties_dict2["Arapahoe"] = 422829

counties_dict2["Denver"] = 463353
counties_dict2["Jefferson"] = 432438

len(counties_dict)

counties_dict.items()

counties_dict.keys()
counties_dict.values()

counties_dict.get("Denver")

counties_dict2["El Paso"] = 461149

counties_dict

OrderedDict((k, queue[k]) for k in counties_dict

counties_dict.pop("Arapahoe")

from collections import OrderedDict
counties_dict = ["Denver", "El Paso", "Jefferson"]

counties_dict

OrderedDict.fromkeys(counties_dict,0)

dict.clear(counties_dict)




counties_dict['Arapahoe'] 

counties_dict.get("Arapahoe")  

print(counties_dict['Arapahoe'])  

print(counties_dict.get("Arapahoe")) 

counties_dict['Arapahoe']

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
