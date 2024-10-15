member = input("Enter a new member: ")

file = open('members.txt', 'r')
members = file.readlines()

file = open('members.txt', 'w')
members.append(member)
file.writelines(members)




