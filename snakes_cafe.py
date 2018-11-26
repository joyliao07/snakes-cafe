from textwrap import dedent
import sys

WIDTH = 100
line_one = 'Welcome to Snake Cafe!'
line_two = 'Please see our menu below.'
line_three = 'To quit any time, type "quit"'


print(dedent(f'''
    {('*' * WIDTH)}
    {('**' + (' ' * ((WIDTH - len('**') - len(line_one))//2 )) + line_one + (' ' * 5) + '**')}

'''))
