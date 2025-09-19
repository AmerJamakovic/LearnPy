# Napisati program u kojem je potrebno unijeti odabrani broj znamenki počevši od znamenke najveće težinske vrijednosti, pa od njih sastaviti i ispisati prirodni broj.
# Unos znamenaka se prekida kada se unese broj manji od 0 ili veći od 9.
# Ispisati poruku ukoliko je dobiveni broj savršen.


def is_int(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_user_number() -> int:
    final_value=0
    while True:
        user_input= input("Enter a number: ")
        if is_int(user_input):
            digit=int(user_input)
            if digit <= 0 or digit>=10:
                break
            final_value = final_value * 10 + digit
        else:
            print("Invalid input! Enter a valid number: ")

    return final_value


def is_perfect_number(number: int) -> bool:
    if number< 2:
        return False
    sum_of_devisors=sum(i for i in range(1, number // 2+1) if number%i==0)
    return sum_of_devisors == number


def main():
    number = get_user_number()
    if is_perfect_number(number):
        print(f"Final number is {number} and it's a perfect number.")
    else:
        print(f"Final number is {number} and it's NOT a perfect number.")


if __name__ == "__main__":
    main()
