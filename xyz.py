class InvalidAge(Exception):
  pass
class InvalidName(Exception):
  pass

def name_age():
  try:
    name = input('Enter name:')
    age = int(input('Enter age:'))
    if len(name) == 1:
      raise InvalidName('This name is invalid')
    elif isinstance(name, int):
      raise InvalidName('This name is invalid')
    elif name[0] == '\t':
      raise InvalidName('This name is invalid')
    elif age < 18:
      raise InvalidAge('This age is not eligible for voting')
    else:
      print('You can go vote')
  except InvalidAge as e:
    print(f'Error : InvalidAge {e}')
  except InvalidName as e:
    print(f'Error : InvalidName {e}')
  except Exception as e:
    print(f'Error : Exception {e}')

name_age()
