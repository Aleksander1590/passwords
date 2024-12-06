password = input("Введите пароль: ") # Ввод пароля

def is_very_long(password): # Функция проверки длины пароля
  if len(password) > 12: # Если длина пароля больше 12 символов
    return True # Возвращаем True
  elif len(password) <= 12: # Если длина пароля меньше или равна 12 символам
    return False # Возвращаем False

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

def password_rating(password): # Функция проверки рейтига пароля
  functions = [is_very_long(password), has_digit(password), has_letters(password), has_upper_letters(password), has_lower_letters(password)]
  for function in functions:
    if function == True:
      score = 
  return score


print("Рейтинг пароля:", password_rating(password)) 
