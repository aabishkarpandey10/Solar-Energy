score = 0

q1 = input("Does your password contain at least 9 characters in length? (y or n): ").strip().lower()
if q1 == 'y':
    score += 1

q2 = input("Does your password contain a mixture of letters and numbers? (y or n): ").strip().lower()
if q2 == 'y':
    score += 1

q3 = input("Does your password contain a mixture of upper and lower case letters? (y or n): ").strip().lower()
if q3 == 'y':
    score += 1

q4 = input("Does your password contain at least one symbol? (y or n): ").strip().lower()
if q4 == 'y':
    score += 1

# Determine the strength of the password based on the number of 'yes' answers
if score == 0 or score == 1:
    print("Your password is considered very weak.")
elif score == 2:
    print("Your password is considered weak.")
elif score == 3:
    print("Your password is considered strong.")
elif score == 4:
    print("Your password is considered very strong.")
score = 0

q1 = input("Does your password contain at least 9 characters in length? (y or n): ").strip().lower()
if q1 == 'y':
    score += 1

q2 = input("Does your password contain a mixture of letters and numbers? (y or n): ").strip().lower()
if q2 == 'y':
    score += 1

q3 = input("Does your password contain a mixture of upper and lower case letters? (y or n): ").strip().lower()
if q3 == 'y':
    score += 1

q4 = input("Does your password contain at least one symbol? (y or n): ").strip().lower()
if q4 == 'y':
    score += 1

if score == 0 or score == 1:
    print("Your password is considered very weak.")
elif score == 2:
    print("Your password is considered weak.")
elif score == 3:
    print("Your password is considered strong.")
elif score == 4:
    print("Your password is considered very strong.")
