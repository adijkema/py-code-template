# ---- [ INFO ]--------------------------------------------------------------------------
# template form for code in python
#   
# Goal: standardize code making and it's output on a device
#       By using a decorator for the main code, you can add in code before and after 
#       i.e. error checking, logging, time functions, process costs, print formatting
# For use in python 2, add; 
#         from __future__ import print_function
# Python version: >= python 3 
# ----------------------------------------------------------------------------------------

# ---- [ INITIALIZE & IMPORTS ] ----------------------------------------------------------
__author__ = 'Your Name'
from os import system
system('clear')                     # clear screen before output
from time import time, localtime, perf_counter, asctime

def decorator_main(func):
    def wrap():
        starttime = perf_counter()
        print(f'[ Code made by: {__author__:<20}                   {asctime(localtime(time()))} ]')
        print(f'{"":-<81}\n\n')

        func()

        print(f'\n\n{"":-<81}')
        print(f'[ END                              code total time costs: {perf_counter() - starttime} ] \n\n')
    return wrap




# ---- [ CODE BLOCK ] --------------------------------------------------------------------------


# ---- [ CLASSES ] -----------------------------------------------------------------------------


# ---- [ FUNCTIONS ] ---------------------------------------------------------------------------
# EXAMPLE FUNCTIONS, TO BE DELETED
# ---- [ whatInstance: returns type of object in format '<type>  ==> <object>'
def whatInstance(obj):
    if isinstance(obj, dict):
        return f'dict  => {obj}'
        
# ---- [ wIn: returns the type of an object in as a string 
def wIn(obj):
    return f'{obj} = {"dict" if isinstance(obj, dict) else "list" if isinstance(obj, list) else "nor dict or list"}'

# ---- [ displ: display give object in nice format
def displ(obj, level=0, space=4, metric=[0]):
    for k, v in obj.items():
        print(f'lvl {level} {whatInstance(k)}')

        if isinstance(v, dict):
            displ(obj, level+1, space=4)
        else:
            print(f'lvl {level} {whatInstance(v)}')


# ---- [ MAIN CODE ] --------------------------------------------------------------------------
@decorator_main
def main():
    # EXAMPLE CODE, TO BE REPLACED
    # ---- initialize some dictionaries
    dict_simple = {'A':{'speed':70,'color':2},'B':{'speed':60,'color':3}}
    dict_complex = {"test":  [{1:3}], 
                    "test2": [(1,{1:'qrest1',2:'qrest2'}), (3,4)],
                    "test3": {(1,2):['abc', 'def', 'ghi'],  (4,5):'def',  "nakje":{1:'nak',2:'naque'}},
                    "test4": 900,
                    }
    dict_2 = {12.98675:  [{1:3}], "test2": [(1,{1:'qrest1',2:'qrest2'}), (3,4)], }

    # ---- print dictionaries as ordered and readable output
    displ(dict_2, 0, 4, [0])
    

if __name__ == '__main__': main()

# ---- [ END CODE BLOCK ] --------------------------------------------------------------------------

