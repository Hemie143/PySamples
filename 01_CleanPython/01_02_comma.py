# Bad example if you want to track changes in git commit
test = ['alpha', 'beta', 'gamma']

# Better example, but ...
test = [
    'alpha',
    'beta',
    'gamma'         # Comma not required, but it's best to add one for further corrections
]

# Bad example, when unexpected concatenation occurs
test = [
    'alpha',
    'beta',
    'gamma'         
    'delta'         # This will create a list with 3 elements, the last one being 'gammadelta'
]

# Correct example
test = [
    'alpha',
    'beta',
    'gamma',
]

# Can later become this:
test = [
    'alpha',
    'beta',
    'gamma',
    'delta',
]