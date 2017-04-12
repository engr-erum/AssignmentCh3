print("I can invite only two people for dinner");
inviteList = ['Aliza', 'Ali', 'Sara', 'Ahmed', 'Saad', 'Aiza'];
for person in inviteList[2:]:
     print("length: "+ str(len(inviteList)));
     personPopped = inviteList.pop();
     print("Sorry " + personPopped +" ... I can't invite you in dinner");print("length else: "+ str(len(inviteList)));
        
print("--------------");
print(inviteList);

for person in inviteList:
	print("Hello "+person+ ", " + "You are still invited.");
				
# delete last two items from list 
for person1 in inviteList[0:]:
    indexPosition = inviteList.index(person1);
    del inviteList[indexPosition];
    
print(inviteList);	

