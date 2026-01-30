guest_list = ['Diana', 'Maria', 'Peter']
not_coming = guest_list[0]
print(f"Hello, unfortunately {not_coming} cannot come.")
guest_list[0] = 'Suzana'
print(f"Hello everyone, I have found a bigger table so I am inviting more people.")
guest_list.insert(0, 'Roman')
guest_list.insert(2, 'Eva')
guest_list.append('Martin')
message = f"Hello {guest_list[0]}, I would like to invite you to dinner today at 7pm."
print(message)
message = f"Hello {guest_list[1]}, I would like to invite you to dinner today at 7pm."
print(message)
message = f"Hello {guest_list[2]}, I would like to invite you to dinner today at 7pm."
print(message)
message = f"Hello {guest_list[3]}, I would like to invite you to dinner today at 7pm."
print(message)
message = f"Hello {guest_list[4]}, I would like to invite you to dinner today at 7pm."
print(message)
message = f"Hello {guest_list[5]}, I would like to invite you to dinner today at 7pm."
print(message)

print(f"\nNumber of people invited to dinner: {len(guest_list)}")
