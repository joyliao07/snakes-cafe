from textwrap import dedent
import sys

WIDTH = 100
line_one = 'Welcome to Snake Cafe!'
line_two = 'Please see our menu below.'
line_three = 'To quit any time, type "quit".'
line_four = 'What would you like to order?'
line_five = 'What else would you like to order?'
status = False
bank =	[
    {
        "dish": "wings",
        "quantity": 0,
    },
    {
        "dish": "cookies",
        "quantity": 0,
    },
]


def welcome():
    print(dedent(f'''
    {('*' * WIDTH)}
    {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_one))//2 )) + line_one + (' ' * ((WIDTH - len('**')*2 - len(line_one))//2 )) + '**')}
    {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_two))//2 )) + line_two + (' ' * ((WIDTH - len('**')*2 - len(line_two))//2 )) + '**')}
    {'**'}
    {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_three))//2 )) + line_three + (' ' * ((WIDTH - len('**')*2 - len(line_three))//2)) + '**')}
    {('*' * WIDTH)}
    {(' ' * WIDTH)}

    {'Appetizers'}
    {('-' * len('Appetizers'))}
    {'Wings'}
    {'Cookies'}
    {'Spring Rolls'}
    {(' ' * WIDTH)}

    {'Entrees'}
    {('-' * len('Entrees'))}
    {'Salmon'}
    {'Steak'}
    {'Meat Tornado'}
    {'A Literal Garden'}
    {(' ' * WIDTH)}

    {'Desserts'}
    {('-' * len('Desserts'))}
    {'Ice Cream'}
    {'Cake'}
    {'Pie'}
    {(' ' * WIDTH)}

    {'Drinks'}
    {('-' * len('Drinks'))}
    {'Coffee'}
    {'Tea'}
    {'Blood of the Innocent'}
    {(' ' * WIDTH)}

    {('*' * WIDTH)}
    {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_four))//2 )) + line_four + (' ' * ((WIDTH - len('**')*2 - len(line_four))//2 )) + '**')}
    {('*' * WIDTH)}
    '''))


def ask_question():
    user_input = input().lower()
    check_input(user_input)
    return user_input




def check_input(user_input):
    match = False
    for item in bank:
        if user_input == 'quit':
            exit()
        if user_input == item['dish']:
            item['quantity'] += 1
            match = True
            print(dedent(f'''
                {('*' * WIDTH)}
                {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_five))//2 )) + line_five + (' ' * ((WIDTH - len('**')*2 - len(line_five))//2 )) + '**')}
                {('*' * WIDTH)}
            '''))
            print(item['dish'])
            print(item['quantity'])
            return user_input

    if match is False:
        print('Sorry, the item you have requested is not on the menu.')
        print(dedent(f'''
            {('*' * WIDTH)}
            {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_five))//2 )) + line_five + (' ' * ((WIDTH - len('**')*2 - len(line_five))//2 )) + '**')}
            {('*' * WIDTH)}
            '''))
        return user_input
    print(item['dish'])
    print(item['quantity'])



def run():
    welcome()
    while status is False:
        user_input = ask_question()





if __name__ == '__main__':
    run()
