guest_list = ['Diana', 'Maria', 'Peter']
not_coming = guest_list[0]
print(f"Hello, unfortunately {not_coming} cannot come.")
guest_list[0] = 'Suzana'
print(f"Hello everyone, I have found a bigger table so I am inviting more people.")
guest_list.insert(0, 'Roman')
guest_list.insert(2, 'Eva')
guest_list.append('Martin')
print("Hello my friends, unfortunately my new large table is not going to come, so I can only invite two people")
not_invited = guest_list.pop(0)
print(f"Hello {not_invited}, I am sorry, you can't come!")
not_invited = guest_list.pop(0)
print(f"Hello {not_invited}, I am sorry, you can't come!")
not_invited = guest_list.pop(0)
print(f"Hello {not_invited}, I am soory, you can't come!")
not_invited = guest_list.pop(0)
print(f"Hello {not_invited}, I am soory, you can't come!")
print(f"Hello {guest_list[0]}, you can still come!")
print(f"Hello {guest_list[1]}, you can still come!")
del guest_list[0]
del guest_list[0]
print(guest_list)
