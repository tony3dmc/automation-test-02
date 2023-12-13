with open('README.md', 'r') as file:
  contents = file.read()
  if 'Hello world' not in contents:
    raise ValueError('Unable to find correct string in README.md')
