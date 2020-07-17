#swaglate any phrase you want

def swaglator(phrase):
    swaglation = ""

    for letter in phrase:
        if letter.lower() in "aeiou" and not(letter.isupper()):
            swaglation = swaglation + ""
        else:
            swaglation = swaglation + letter
    return swaglation

exit_swaglator = False

while exit_swaglator == False:
    print(swaglator(input("Swaglate your phrase: ")))
    
    exit_input = input("Do you want to swaglate another phrase? [y,n]")
    
    if exit_input.lower() == "y":
        exit_swaglator = False
    elif exit_input.lower() == "n":
        exit_swaglator = True
    else:
        correct_answer = False
        while correct_answer == False:
            false_exit_input = input("Press \"y\" for yes or \"n\" for no.")
            
            if false_exit_input.lower() == "y":
                correct_answer = True
                exit_swaglator = False
            elif false_exit_input.lower() == "n":
                correct_answer = True
                exit_swaglator = True
            else:
                correct_answer = False