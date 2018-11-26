from textwrap import dedent
import sys

WIDTH = 100
line_one = 'Welcome to Snake Cafe!'
line_two = 'Please see our menu below.'
line_three = 'To quit any time, type "quit".'
line_four = 'What would you like to order?'


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








def run():
    welcome()


if __name__ == '__main__':
    run()
