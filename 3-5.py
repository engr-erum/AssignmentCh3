
inviteList = ["Ali" , "Sara" , "Saad"];
print("First Set of Invitation");
print("------------------------");
for invitePerson in inviteList:
	print("Hello " + invitePerson + "," + " I would like to invite you for today's dinner.");
personCantMake = "Sara";

print("\n" + personCantMake + " cannot make dinner.");
# trying to get index for not coming person
indexCantMake = inviteList.index(personCantMake);
# alter list index name
inviteList[indexCantMake] = "Ahmed";

print("\n Modified List");
print("-------------");
print(inviteList);
print("\n Second Set of Invitation");
print("------------------------");
for invitePerson in inviteList:
	print("Hello " + invitePerson + "," + " I would like to invite you for today's dinner.");
