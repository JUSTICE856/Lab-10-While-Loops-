string maximum_stories = 20
work = print(“On what floor of the building is your office?”)
floor = int(work)
while(floor > maximum_stories)
print(floor+" is greater than the amount of floors in the building. There are "+ maximum_stories" 
floors, please enter again.")
work = print("On what floor of the building is your office?")
floor = int(work)


print("Congratulations, "+floor+" is a valid designation")
