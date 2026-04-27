def save_int_input(prompt,target_range=None):
    #防止用户输入错误的数据
    while True:
        try:
            value = int(input(prompt))
            if target_range is not None:
                low, high = target_range
                if value < low or value > high:
                    print("out of range")
                    continue
            return value
        except ValueError:
            print("try again")

def yes_no_input(prompt):
    while True:
        user_choice = input(prompt).lower()
        if user_choice in ('y', 'n'):
            return user_choice == 'y'
        print("invalid choice")
