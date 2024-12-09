def is_very_long(password): 
    if not len(password) < 12:
      return True 

def has_digit(password): 
    return any(symbol.isdigit() for symbol in password) 

def has_letters(password):
    return any(symbol.isalpha() for symbol in password) 

def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)

def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)

def has_symbols(password):
    return any(not symbol.isdigit() and not symbol.isalpha() for symbol in password)

def password_rating(password): 
    functions = [
    is_very_long(password), 
    has_digit(password), 
    has_letters(password), 
    has_upper_letters(password), has_lower_letters(password)]
    score = 0
    for function in functions:
        if function:
            score += 2
    return score

def main():
    password = input("Введите пароль: ") 
    print("Рейтинг пароля:", password_rating(password)) 

if __name__ == '__main__':
    main()
