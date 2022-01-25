age: int = 17

is_allowed_to_vote: bool = age >= 18

if is_allowed_to_vote:
    print("Вы имеете право голосовать")
    difference = age - 18
    print("уже как " + str(difference) + " лет")
else:
    print("Увы, вы не можете голосовать")
difference = 18 - age
print("Приходите через " + str(difference) + " лет")
