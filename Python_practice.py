'''
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes/total_votes)*100

message_to_candidate = (f"You recieved {my_votes: ,} number of votes. "
                     f"The total number of votes in the election was {total_votes: ,}. "
                     f"You recieved {(my_votes/total_votes) *100: .2f}% of the total votes")


print(message_to_candidate)
'''



# functions
# def - define a funciton
# name of the function - print_hello()
# arguments - data put in the parentheses of your function to use. 

def print_hello(): 
    print("Hello!")


print_hello() # calls out the funciton to be run




#counties = ["Arapahoe", "Denver", "Jefferson"]



#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
    #print(f"{county} county has  {voters: ,} registered voters." ) 

from email import message


voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, 
               {"county": "Denver", "registered_voters": 463353}, 
               {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data: 
    county = county_dict["county"]
    reg_vot = county_dict["registered_voters"]
    message = (f"{county} county has {reg_vot: ,} registered voters")
    print(message)
#for county_dict in voting_data: 
  #  print(county_dict["county"])


'''
for i in range(len(voting_data)):  
    print(f"{voting_data[i]["county"]} ")
'''
#for county, voters in counties_dict.items(): 
   # print(county +  " county has " + str(voters)+ " registered voters. ")
#for i in range(5): 
    #print(i)

#for i in range(len(counties)): 
    #print(counties[i])


##counties = ["Arapahoe", "Denver", "Jefferson"]
#if "Arapahoe" in counties or "El Paso" in counties: 
    #print("Arapahoe or El Paso are in the list of counties")
#else: 
    #print("Arapahoe and El Paso are not in the list of counties")
    