password = input("Введите пароль: ")

def is_very_long(password): 
  if len(password) > 12: 
    return True 
  elif len(password) <= 12: 
    return False 

def has_digit(password): 
  for symbol in password: 
    if symbol.isdigit(): 
      return True 
    return False 

def has_letters(password):
  for symbol in password:
    if symbol.isalpha():
      return True
    return False

def has_upper_letters(password):
    for symbol in password:
      if symbol.isupper():
        return True
    return False

def has_lower_letters(password):
    for symbol in password:
        if symbol.islower():
            return True
    return False

def password_rating(password):
  functions = [is_very_long(password), has_digit(password), has_letters(password), has_upper_letters(password), has_lower_letters(password)]
  score = 0
  completed_functions = 
  for function in functions:
    if function == True:
        score = completed_functions*2
  return score 
 

print("Рейтинг пароля:", password_rating(password)) 
