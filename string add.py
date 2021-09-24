Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='Bangla'
>>> a
'Bangla'
>>> b='desh'
>>> b
'desh'
>>> #akhon ay alada string duita k amr jodi akotre likhte chai tahole niche lokkho kori
>>> a+b
'Bangladesh'
>>> #akhon amra 3ta variable nibo abong tader add korbo
>>> x='Barishal'
>>> y='Dhaka'
>>> z='sylhet'
>>> x+'-'+y'-'+z
SyntaxError: invalid syntax
>>> x+'-'+y+'-'+z
'Barishal-Dhaka-sylhet'
>>> amra kintu ay kazta aro shohoz a korte partam
SyntaxError: invalid syntax
>>> amra kintu ay kazta aro shohoz a korte partam join() function diye
SyntaxError: invalid syntax
>>> x='Barishal'
>>> y='Dhaka'
>>> z='sylhet'
>>> '-'.join((x,y,z))
'Barishal-Dhaka-sylhet'
>>> 