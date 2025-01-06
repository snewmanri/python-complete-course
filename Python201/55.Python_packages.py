#pip install the package name
#from packagename import thing1, thing2, etc
from colorama import init, Fore, Back, Style # type: ignore
init()


print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')