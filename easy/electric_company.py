# Electric Company
# Create a function that given a list which represents street 
# lights given as a parameter(l_street), determine if an outage has occurred. 
# A street with a total number of “F” greater than or equal to 2 returns 
# “Outage”, anything below returns “Power”
# Example Input: [ "T", "F", "F", "F" ]
# Example Output: "Outage"


def streetLights(l_street):
   effs = 0
   for val in l_street:
       if val == "F":
           effs += 1
   if effs >= 2:
       return "Outage"
   else:
       return "Power"


print(streetLights([ "T", "F", "F", "F" ]))