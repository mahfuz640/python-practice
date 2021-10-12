Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #akhon porjonto amra akta item e list a add korte perese but akhon amra jodi chai je akotre onk item add korte list a tokhon amra ki korbo tokhon amra expend function use korbo
>>> a=['rice','potato',343,'cucumber','finger'464.45564,'new']
SyntaxError: invalid syntax
>>> a=['rice','potato',343,'cucumber','finger',464.45564,'new']
>>> a
['rice', 'potato', 343, 'cucumber', 'finger', 464.45564, 'new']
>>> a.extend(['a','b','c',6546.54])
>>> a
['rice', 'potato', 343, 'cucumber', 'finger', 464.45564, 'new', 'a', 'b', 'c', 6546.54]
>>> #akhon ashe ato jhamelar kintu kono dorkar e nai amra chaile kono list k o list ar shate jog korte pari
>>> a+['s','d','h']
['rice', 'potato', 343, 'cucumber', 'finger', 464.45564, 'new', 'a', 'b', 'c', 6546.54, 's', 'd', 'h']
>>> 