list_guest = ['Tesla', 'Koch', 'Kirchow', 'Newton']
missing_guest = list_guest.pop(1)
list_guest.insert(1, 'Pupin')
list_guest.insert(0, 'Curie')
list_guest.insert(2, 'Galileo')
list_guest.append('Einstein')
message = "Mr." + list_guest[0] + ", I would like to invite you to a dinner."
print(message)
message = "Mr." + list_guest[1] + ", I would like to invite you to a dinner."
print(message)
message = "Mr." + list_guest[2] + ", I would like to invite you to a dinner."
print(message)
message = "Mr." + list_guest[3] + ", I would like to invite you to a dinner."
print(message)
message = "Mr." + missing_guest + ", unfortunately can't make it."
print(message)
message = "Great news, I found a bigger table so more guests can come!"
print(message)
