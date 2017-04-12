
inviteList = ["Ali" , "Sara" , "Saad"];
print("First Set of Invitation");
print("------------------------");
for invitePerson in inviteList:
	print("Hello " + invitePerson + "," + " I would like to invite you for today's dinner.");
personCantMake = "Sara";
print("");
print(personCantMake + " cannot make dinner.");
# trying to get index for not coming person
indexCantMake = inviteList.index(personCantMake);
# alter list index name
inviteList[indexCantMake] = "Ahmed";
print("");
print("Modified List");
print("-------------");
print(inviteList);
print("");
print("Second Set of Invitation");
print("------------------------");
for invitePerson in inviteList:
	print("Hello " + invitePerson + "," + " I would like to invite you for today's dinner.");
