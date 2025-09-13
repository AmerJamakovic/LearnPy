#Napisati program u kojem je potrebno unijeti odabrani broj znamenki počevši od znamenke najveće težinske vrijednosti, pa od njih sastaviti i ispisati prirodni broj.
#Unos znamenaka se prekida kada se unese broj manji od 0 ili veći od 9.
#Ispisati poruku ukoliko je dobiveni broj savršen.

def IsString(value: str)->bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def UserInputFunc(input_valid_for_ending:bool=False,final_value:int=0)->int:
    while not input_valid_for_ending:
        user_input = input("Enter a number: ")
        if IsString(user_input):
            if int(user_input) <= 0 or int(user_input) >= 10:
                input_valid_for_ending = True
                break
            else:
                final_value *= 10
                final_value += int(user_input)
        else:
            print("Invalid input")

    return final_value

def IsPerfectNumber(number:int)->bool:
    ifSameTrue=0
    for value in range(1,float.__floor__(number/2)+1):
        if number%value==0:
            ifSameTrue+=value
        else:
            continue
    if ifSameTrue==number:
        return True
    else:
        return False


def main():
    number = UserInputFunc()
    if IsPerfectNumber(number):
        print(f"Final number is {number} and it's a perfect number.")
    else:
        print(f"Final number is {number} and it's NOT a perfect number.")

main()
