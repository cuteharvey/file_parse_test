import os

def info(msg):
    """Adding this class in case you want to do something else with the LOG. eg. print in a file or send somewhere"""
    # doing this will save you time when you want to modify print.
    # you just need to modify here instead of modifying all tests.

    if os.environ.get('PRINT_CONSOLE') != 'FALSE':  # set this env to false if you don't want to print in console
        print("INFO: " + str(msg))