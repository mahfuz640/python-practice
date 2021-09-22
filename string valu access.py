Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='Banlgadesh'
>>> a[:2]
'Ba'
>>> #a[:2] diye string ar 1st duita letter show korte bola hoyese
>>> a[2:]
'nlgadesh'
>>> #a[2:] diye string ar 1st duita letter bad diye show korte bola hoyese
>>> 
>>> a[-1]
'h'
>>> a[-2]
's'
>>> a[-1,-2]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[-1,-2]
TypeError: string indices must be integers
>>> a[-1]
'h'
>>> a[-2]
's'
>>> #a[-1],a[-2]kono string ar shesh ar dik theke 1st letter 2nd letter output pawar jonno use hoi.