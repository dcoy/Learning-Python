# This will demonstrate default argument values.  For some functions,
# you may want to make some parameters optional and use default values
# in the event the user does not provide values.

def say(message, times=1):
    print(message * times)

say('Hello')
say('World', 5)
