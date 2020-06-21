import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

counties_list = []
county_votes_dict = {}
largest_county_turnout = ""
total_votes = 0
votes_in_county = 0 
largest_county_turnout_votes = 0 
largest_county_turnout_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        county_name = row[1]
        if county_name not in counties_list:
            counties_list.append(county_name)
            county_votes_dict[county_name] = 0
        county_votes_dict[county_name] +=1
    
    for county in county_votes_dict:
        votes_in_county = county_votes_dict[county]
        county_percentage = int(votes_in_county) / int(total_votes)*100
        county_results = (f"\n{county}: {county_percentage:.1f}% ({votes_in_county: ,} )\n")
        print(county_results)
        if (votes_in_county > largest_county_turnout_votes) and (county_percentage > largest_county_turnout_percentage):
            largest_county_turnout_votes = votes_in_county
            largest_county_turnout_percentage = county_percentage
            largest_county_turnout = county
    largest_county_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n")
    print(largest_county_turnout_summary)
