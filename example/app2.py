# try:
#     from . import utils
# except ImportError:
#     print("Import Error !")


import utils

numbers = [10, 3, 5, 50, 2, 4, 89]
maximum = utils.find_max(numbers)
print(maximum)