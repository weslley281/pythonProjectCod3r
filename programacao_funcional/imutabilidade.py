from locale import setlocale, LC_ALL
from calendar import month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR')
print(month_name[1])