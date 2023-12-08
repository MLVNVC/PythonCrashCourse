list_guest = ['Tesla', 'Koch', 'Kirchow']
message = "I can invite only 2 people. "
print(message)
deleted = list_guest.pop()
message = "Mr." + list_guest[0] + ", I would like to invite you to a dinner."
print(message)
message = "Mr." + list_guest[1] + ", I would like to invite you to a dinner."
print(message)
message = "Mr." + deleted + ", sorry."
print(message)
