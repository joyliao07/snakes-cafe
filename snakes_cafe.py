"""This module design the snake-cafe menu program."""
from textwrap import dedent
import sys

WIDTH = 100
status = False
bank = [
    {
        "dish": "wings",
        "quantity": 0,
    },
    {
        "dish": "cookies",
        "quantity": 0,
    },
    {
        "dish": "spring rolls",
        "quantity": 0,
    },
    {
        "dish": "salmon",
        "quantity": 0,
    },
    {
        "dish": "steak",
        "quantity": 0,
    },
    {
        "dish": "meat tornado",
        "quantity": 0,
    },
    {
        "dish": "a literal garden",
        "quantity": 0,
    },
    {
        "dish": "ice cream",
        "quantity": 0,
    },
    {
        "dish": "cake",
        "quantity": 0,
    },
    {
        "dish": "pie",
        "quantity": 0,
    },
    {
        "dish": "coffee",
        "quantity": 0,
    },
    {
        "dish": "tea",
        "quantity": 0,
    },
    {
        "dish": "blood of the innocent",
        "quantity": 0,
    },
]


def welcome():
    """To greet the users and start the promp to take input."""
    line_one = 'Welcome to Snake Cafe!'
    line_two = 'Please see our menu below.'
    line_three = 'To quit any time, type "quit".'
    line_four = 'What would you like to order?'
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
    """To define user_input and pass to the next function."""
    user_input = input().lower()
    check_input(user_input)
    return user_input


def check_input(user_input):
    """Per user_input, decide the path to go down."""
    line_five = 'What else would you like to order?'
    match = False
    for item in bank:
        if user_input == 'quit':
            exit()
        if user_input == item['dish']:
            item['quantity'] += 1
            match = True
            print(dedent(f'''
                {(str(item['quantity']) + ' items of ' + (item['dish']) + ' have been added to your meal')}
            '''))
            print(dedent(f'''
                {('*' * WIDTH)}
                {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_five))//2 )) + line_five + (' ' * ((WIDTH - len('**')*2 - len(line_five))//2 )) + '**')}
                {('*' * WIDTH)}
            '''))
            return user_input

    if match is False:
        print('Sorry, the item you have requested is not on the menu.')
        print(dedent(f'''
            {('*' * WIDTH)}
            {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_five))//2 )) + line_five + (' ' * ((WIDTH - len('**')*2 - len(line_five))//2 )) + '**')}
            {('*' * WIDTH)}
            '''))
        return user_input


def run():
    """To invoke welcome function."""
    welcome()
    while status is False:
        user_input = ask_question()


if __name__ == '__main__':
    run()
