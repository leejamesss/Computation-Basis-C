
lst=input().split(",")
def isvalid(password):
      if len(password)<6 or len(password)>12:
         return False
      if not any(char.isdigit() for char in password):
         return False
      if not any(char.isupper() for char in password):
         return False
      if not any(char.islower() for char in password):
         return False
      if not any(char in ["@","#","$","!"] for char in password):
         return False
      if any((not char.isdigit()) and (not char.isupper()) and (not char.islower()) and (not char in ["@","#","$","!"]) for char in password):
         return False
      return True
for password in lst:
    if isvalid(password):
       print(password)
    
