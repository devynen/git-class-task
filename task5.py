"""
    You're cleaning up your phone's contact list and organizing your close friends from Jos.
    Your friends list is: friends = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]
    
    1. You made a new close friend "Kemi" and want to add her between "John" and "Mary".
    2. "Daniel" moved to Lagos and you don't talk anymore, so remove him from your close friends list.
    3. "Aisha" got married and now goes by "Aisha_M". Update her name in the list.
    4. You want to add your cousin "Zainab" at the end of the list.
    5. Create a new list with only the first 3 friends from your updated list and display it.
    6. Find out what position "Paul" is in your final friends list (remember: position counting starts from 1 for humans!).
    7. arrange your contacts in Descending Alphabetical Order using.
"""

friends = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]
print(friends)

#to add kemi between jhon and mary
friends.insert(4,"kemi")
print(friends)

#to remove Daniel
friends.remove(friends[1])
print(friends)

#to change Aisha name
friends[0]="Aisha M"
print(friends)

#to add zainab at the end
friends.append("Zainab")
print(friends)

#new list with first three list
new_friends=friends[0:3]
print(new_friends)

#find where paul is
paul=friends.index("Paul")
print(f"pauls position in the list is:", paul)


#arrange contacts alpabetically
friends.sort
print(friends)


