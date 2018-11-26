from textwrap import dedent
import sys

WIDTH = 100
line_one = 'Welcome to Snake Cafe!'
line_two = 'Please see our menu below.'
line_three = 'To quit any time, type "quit".'


print(dedent(f'''
    {('*' * WIDTH)}
    {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_one))//2 )) + line_one + (' ' * ((WIDTH - len('**')*2 - len(line_one))//2 )) + '**')}
    {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_two))//2 )) + line_two + (' ' * ((WIDTH - len('**')*2 - len(line_two))//2 )) + '**')}
    {'**'}
    {('**' + (' ' * ((WIDTH - len('**')*2 - len(line_three))//2 )) + line_three + (' ' * ((WIDTH - len('**')*2 - len(line_three))//2)) + '**')}
    {('*' * WIDTH)}
'''))
