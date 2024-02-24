from random import choice

print('This is a Random Password Generator by: APersonIThink \n')

charecters_letters = choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'])
charecters_num = int(choice([1, 2, 3, 4, 5, 6, 7, 8, 9, ]))
charecters_special = choice(['!', '@', '#', '%', '^', '&', '*', '(', ')'])
charecters_letters2 = choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'])
charecters_num2 = int(choice([1, 2, 3, 4, 5, 6, 7, 8, 9, ]))
charecters_special2 = choice(['!', '@', '#', '%', '^', '&', '*', '(', ')'])
charecters_letters3 = choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'])
charecters_num3 = int(choice([1, 2, 3, 4, 5, 6, 7, 8, 9, ]))
charecters_special3 = choice(['!', '@', '#', '%', '^', '&', '*', '(', ')'])

print('Your Password Is:', charecters_letters,charecters_special, charecters_letters2, charecters_num2, charecters_special2, charecters_num3, charecters_special3, charecters_letters2, charecters_letters,charecters_special, charecters_letters2, charecters_num2, charecters_special2, charecters_num3, charecters_special3, charecters_letters2, charecters_letters,charecters_special, charecters_letters2, charecters_num2, charecters_special2, charecters_num3, charecters_special3, charecters_letters2)

password = str((charecters_letters,charecters_special, charecters_letters2, charecters_num2, charecters_special2, charecters_num3, charecters_special3, charecters_letters2, charecters_letters,charecters_special, charecters_letters2, charecters_num2, charecters_special2, charecters_num3, charecters_special3, charecters_letters2, charecters_letters,charecters_special, charecters_letters2, charecters_num2, charecters_special2, charecters_num3, charecters_special3, charecters_letters2))

print(password)

pass_save = input('Do You Want To Save This Passcode To a File?: ')
if pass_save == 'yes' or 'Yes':
    pass_save_name = input('What Do You Want To Call The File INCLUDE FILE FORMAT: ')
    with open(pass_save_name, 'x') as file:
        with open(pass_save_name, 'w') as password_saved:
            password_saved.write(password)