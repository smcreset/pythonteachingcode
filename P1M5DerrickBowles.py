#adding_report()

a_mode = input('What would you like to do?\nTo print all numbers entered and get the total, type "A"\nTo just print the total, type "T"\n')
items = ""
total = 0
acc_par = "a, t"
loops = 0

def adding_report(mode):
    global a_mode
    global items
    global total
    global loops
    while loops == 0:
        if a_mode.lower() == "a":
            while True:
                ent_num = input('Enter a number or type "Q" to quit: ')
                if ent_num.isnumeric():
                    items = items + ent_num + "\n"
                    total = int(total) + int(ent_num)
                elif ent_num.lower().startswith("q"):
                    print(items)
                    print("Total")
                    print(total)
                    loops += 1
                    break
                else:
                    print('Input is invalid')
                    loops += 1
                    break
        elif a_mode.lower() in acc_par == False:
            a_mode = input('Please type either "A" or "T": ')
        elif a_mode.lower() == "t":
            while True:
                ent_num = input('Enter a number or type "Q" to quit: ')
                if ent_num.isnumeric():
                    all_num = items + ent_num + "\n"
                    total = int(total) + int(ent_num)
                elif ent_num.lower().startswith("q"):
                    print("Total")
                    print(total)
                    loops += 1
                    break
                else:
                    print('Input is invalid.')
                    loops += 1
                    break

adding_report(a_mode)
