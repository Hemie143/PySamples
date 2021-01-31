name = 'John'
status = 'OK'

# Traditional string formatting
print('Hello, %s' % name)
print('Hello, %(name)s')

# Format string formatting
print('Hello, {}'.format(name))
print('Hello, {name}. The status is {status}'.format(name=name, status=status))

# f-string
print(f'Hello, {name}. The status is {status}')

# Templates
from string import Template
t = Template('Hello, $name. The status is $status')
print(t.substitute(name=name, status=status))

