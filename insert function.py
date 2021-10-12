Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #append function diye amra kono item list ar last a jog korte pari
>>> #but but but kotha ase ami jodi list ar shurute kisu add korte chai tokhon ....ha tokhon amra insert() function use korbo.
>>> b=['rice','potato',343,4523]
.
>>>  b=['rice','potato',343,4523.155,'cucumber','finger']
 
SyntaxError: unexpected indent
>>> b=['rice','potato',343,4523.155,'cucumber','finger']

>>> #ami akhon list index number 1 ar jagai new kisu add korbo
>>> b.insert(1,'onion')
>>> b
['rice', 'onion', 'potato', 343, 4523.155, 'cucumber', 'finger']
>>> 