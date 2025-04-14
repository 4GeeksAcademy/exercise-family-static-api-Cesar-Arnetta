"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 0
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

# First we check if the value member's method have an id inside of init list of self.members. If not, we use the _generate_id method
# to add it. Last we check if the member have the last name, if not we use de init value of last name, becauase all are part of the same family.
# Finally we use the python's method append to add this member to the family
# The final return is important to close the method 

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()
        if "last_name" not in member:
            member["last_name"] = self.last_name
        self._members.append(member)
        return member

# Using a loop for member in  self._members we create a conditional if members["id"] is the same of the id's parameter, we finally use
# the remove python's method to members

    def delete_member(self, id):
       for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return
            
# Using a loop for member in  self._members we create a conditional if members["id"] is the same of the id's parameter, we finally use
# return the chose member if there is no existed member, the metjod return None 

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None 

    # This method is done, it returns a list with all the family members / it's the default method of the exercise
    def get_all_members(self):
        return self._members
    
# These are the testing lines 

# John Jackson
# 33 Years old
# Lucky Numbers: 7, 13, 22

# Jane Jackson
# 35 Years old
# Lucky Numbers: 10, 14, 3

# Jimmy Jackson
# 5 Years old
# Lucky Numbers: 1

# family = FamilyStructure("Jackson")

# family.add_member({
#     "first_name": "Jane",
#     "age": 35,
#     "lucky_numbers": [10, 14, 3]
# })

# # Get a member by ID
# member = family.get_member(1)  # Should return Jhon Jackson
# print(member)

# members = family.get_all_members()
# print(members)

# # Delete a member by ID
# family.delete_member(1)  # Removes Jhon Jackson who is declared in the __init__ 

# # Get all members after deletion withou Jhon
# members = family.get_all_members()
# print(members)