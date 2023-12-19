# Dictionary

## How to maintain the order of inserted/decalred keys/values pair.
- Form Python 3.6 onwards, the standard dict type maintains insertion order by default
- Before Python 3.6 you can use
  - [collections.OrderedDict()](https://mail.python.org/pipermail/python-dev/2017-December/151283.html)
  - collections.Counter() : we can increment the value of key, without declaration, in dict we will get "key error"

```python
>>> import collections
>>> c= collections.Counter()

>>> d['a'] += 1
/usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.15) or chardet (3.0.4) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'a'
>>> c['a'] +=1

```
 [How Dict is implemented](https://mail.python.org/pipermail/python-dev/2012-December/123028.html)

 
# List
# Tuple
# Set
# Function
# Lambda function
# Class
# Static Method
# Class Method
# Iterator
# Generator
# Decorator
- Function based
- Class Based
# except .. finally .. else
# for .. else
