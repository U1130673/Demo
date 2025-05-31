Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name = ['Sean Flanagan']
>>> print (name)
['Sean Flanagan']
>>> nums = [1,2,3,4,5,6,7,8,9]
>>> squared = [x**2 for x in nums]
>>> print squared
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print (squared)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
