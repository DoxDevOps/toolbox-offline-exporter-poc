# coding=utf-8

from utils.validate_emr_data import append_other_apps


def choose_app():
    """
    a function that prompts a ser to enter other apps installed at a facility
    :return:
    """
    print("Please select other apps installed !")
    print("1. NONE \n2. ANC \n3. Maternity \n4. HTS \n5. OPD \n")
    app_id = int(raw_input("Enter your Selection number: "))
    check_chosen_app(app_id)
    return True


def check_chosen_app(app_id):
    """
    checks for the digits entered by user if they are valid
    :param app_id:
    """
    while True:
        try:
            if app_id > 7:
                print("The number selected is not on the list, Please try again:")
                continue
            if app_id < 0:
                print("Please Select a POSITIVE number:")
                continue
            if app_id == 1:
                break
            append_other_apps(app_id)
            choose_another_app()
        except ValueError:
            print("\nPlease enter a valid number")
            continue
        else:
            break


def choose_another_app():
    """
    prompts a user to select another module / app installed at a facility
    """
    while True:
        answer = raw_input("Do yo want to add another Module(yes/no, y/n :)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            choose_app()  # start all over
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            break
        else:
            print('Please enter yes or no')
            continue
