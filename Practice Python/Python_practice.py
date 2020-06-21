print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]

# this statement is true and returns Denver
if counties[1] == 'Denver': 
    print(counties[1])

# this returns an IndexError because the list index is out of range
#if counties[3] != 'Jefferson':
    #print(counties[2])

# this prints true because Arapahoe is in the counties list
if "Arapahoe" in counties: 
    print("True") 
else: 
    print("False")

# this prints true because El Paso is not in the counties list
if "El Paso" not in counties:
    print("True")
else: 
    print("False")

# the output will be "El Paso is not in the list of counties."
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

# Arapahoe is in the counties list, which is true
# But, El Paso is not in the counties list, which is false
# the compound expression is false
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# decision statement checks if either Arapahoe or El Paso is "true"
# Arapahoe is in the counties list, which is true
# But, El Paso is not in the counties list, which is false
# the compound expression is true
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list fo counties.")

# Arapahoe in counties is "true"
# El Paso is not in counties is "true"
# "Only Arapahoe is in the list of counties" will be printed
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# Practice For Loops
for county in counties:
    print(county)
# the county variable is declared and set equal to the first item in the list of counties
# the loop will prin "Arapahoe", then "Denver", then "Jefferson"

# Practice range() function
for i in range(len(counties)):
    print(counties[i])
# the variable i is used to indicate the index (values 0, 1, 2)
# inside the range() function, we get the length of the list (integer 3)
# the variable i = 0 for the first index and is passed into the statement
# i = 0 and "Arapahoe is printed"
# process repeats until all 3 items are printed 

# iterate through a tuple
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

for county in counties_tuple:
    print(county)

# iterate through a dictionary 
counties_dict = {"Arapahoe" : 422829, "Denver" : 463353, "Jefferson" : 432438}

# get the keys of a dictionary 
for county in counties_dict:
    print(county)
# you can also use the keys() method
for county in counties_dict.keys():
    print(county)
# in the keys method, it does not matter what variable name we use in for loop
# reminder: keys() will print each key in order 

# get the values of a dictionary 
for voters in counties_dict.values():
    print(voters)
# in the values method, it does not matter what variable name we use in for loop
# reminder: values() will print each value in order 
# you can also use the dictionary_name[key] method
for county in counties_dict:
    print(counties_dict[county])
# you can also use the get() method
for county in counties_dict:
    print(counties_dict.get(county))

# get the key-value pairs of a dictionary 
# use the items method: we get the "key" and "value" for each dictionary
for county, voters in counties_dict.items():
    print(county, voters)
# the output will be each key and value in order 
for county, voters in counties_dict.items():
    print(str(county) + " county has " + str(voters) + " registered voters.")
# use f-string method instead
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# get each dictionary in a list of dictionaries 
voting_data = [{"county": "Arapahoe", "registered_voters" : 422829},
 {"county": "Denver", "registered_voters" : 463353},
  {"county" : "Jefferson", "registered_voters" : 432438 }]

for counties_dict in voting_data:
    print(counties_dict)
# this will print each dictionary to a separate line

# since this is a list of dictionaries, use the range() function
for i in range(len(voting_data)):
    print(voting_data[i])

# get the values from the list of dictionaries 
# this will require a nested for loop
for county_dict in voting_data: #retrieves each dictionary 
    for value in county_dict.values(): #references the data to get each value
        print(value) # output is the value from each key

# retrieve # of voters from each dictionary 
for counties_dict in voting_data:
    print(counties_dict['registered_voters'])

# retrieve county name from each dictionary 
for counties_dict in voting_data:
    print(counties_dict['county'])

# Practice f-strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
# original code
percentage_votes = (my_votes / total_votes) * 100
print("I recieved " + str(percentage_votes) + "% of the total votes.")
# using f-string
print(f"I recieved {my_votes / total_votes * 100:.2f}% of the total votes.")
# inside the {}, the f-string performs the calculation 

# use multiple f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
message_to_candidate = (
    f"You receieved {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You recieved {candidate_votes / total_votes * 100:.2f}% of the total votes."
)
print(message_to_candidate)

counties_dict = {"Arapahoe" : 422829, "Denver" : 463353, "Jefferson" : 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county": "Arapahoe", "registered_voters" : 422829},
 {"county": "Denver", "registered_voters" : 463353},
  {"county" : "Jefferson", "registered_voters" : 432438 }]

for counties_dict in voting_data:
    print(f"{counties_dict['county']} county has {counties_dict['registered_voters']:,} registered voters.")