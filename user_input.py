
##
# The file to handle logic surrounding user keyboard inputs

#
##

keys_down = set()

def is_key_pressed(key):
  return key in keys_down # check to see if a key is being pressed