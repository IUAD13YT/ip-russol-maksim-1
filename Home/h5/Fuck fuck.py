line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'


# print(ord('A'))
# A = ord('A')
# print(ord('Z'))
# Z = ord('Z')
# simv = list(map(chr(range(65, 91))))
# print(simv)
# symbol = list(map(lambda x: chr(x), list(range(A, Z+1))))  # Преобразуем список из кодов ANSI в список букв A-Z
# line_2 = list(line)



# '''import re
# x = '5/7 - 2/3'
# print(x)
# # x = x.split(' ')
# z = eval(x)
# print(eval(x))
# from fractions import Fraction
# # pattern = '[0-9]'
# # found = re.findall()
#
# # from decimal import Decimal
# # Fraction(Decimal('7.7'))
# # Fraction(77, 10)
# answ = (float.as_integer_ratio(eval(x)))
# print(Fraction.from_float(z))
# b = []
# b.append(Fraction.from_float(z))
# print(b)
# from decimal import Decimal
# Fraction.from_decimal(Decimal(z))
# print(Fraction(Fraction.from_decimal(Decimal(z))))'''
# def modify(x):
#     lst = [el**2 for el in x]
#     return lst
# my_list = [1,2,3]
# mod_list = modify(my_list)
# print(my_list)
# print(mod_list)
line = ['444', '555', '000', '999', '000', '666', '555', '888', '111', '444', '555', '666', '999', '444', '777', '333', '444', '888', '333', '222', '888', '000', '888', '111', '777']
m=max(map(len,line))
print(m)
for i in line:
       if len(i) == m:
              print(i, end=' ')