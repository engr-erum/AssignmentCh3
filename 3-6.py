
inviteList = ["Ali" , "Ahmed" , "Saad"];

#insert guest in start of list
inviteList.insert(0,"Aliza");

# find middle list position
middleListPosition = len(inviteList)/ 2;

#add one more person in the mid of list
inviteList.insert(middleListPosition , "Sara");

#append one more person in the end of list
inviteList.append("Aiza");

print(inviteList);
for invitePerson in inviteList:
	 print("Hello " + invitePerson + "," + " I would like to invite you for today's dinner.");
  
print("--------------------------------------------");
print("We have got more space in our dinning table");
