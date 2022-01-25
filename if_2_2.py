age: int = 17

if age <= 5:
    print("Детский сад")
else:
    if age <= 16:
        print("Школа")
    else:
        if age <= 21:
            print("Университет")
        else:
            if age <= 65:
                print("Когда же ты уже найдешь работу и съедешь")
            else:
                if age <= 100:
                    print ("Отдыхай")
                else:
                    print ("Да ты шутишь!")
