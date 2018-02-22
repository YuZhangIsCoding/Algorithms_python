# Illustration for ks primitives

This problem set introduces 8-bit and 16-bit operations. Here are some basics
concepts from the code.

1. Singletons
The codes used the notion of [singletons](https://en.wikipedia.org/wiki/Singleton_pattern),
which means that there is one and only one object for a particular type. In this case, one and 
only one Byte object is created for a value ranged from 0x00 to 0xFF.
To me, it's like a dictionary that we build initially and can lookup the digits thereafter.
This makes sense because instead of creating a millions of Byte objects for each number, we can 
now just create a static storage of the digits we needed and access them through pointers.

1. Byte
    * Byte is an class object that has following attributes:
        * _byte: stores the value, which we can see as decimal value, ranging from 0x00 to 0xFF.
        * _hex: stores 2 hexadecimal digits, from 00 to FF.
        * _word: initiated with None, but was later assigned a Word object after the 
Word singletons are built.    
    * Besides the previous attributes, the Byte class also has a list to store
all the singleton Byte instances:
        * _bytes: a lis that stores all the Byte objects, from 0x00 to 0xFF
        * this list only initialize once and can be used for all the 8-bit digits
    * When comparing 2 Byte objects, the builtin isinstance() can help to identify if the two
are of the same class
    * Since the Byte objects in \_bytes are all singletons, no need to implement 
\_\_eq\_\_, \_\_ne\_\_ and \_\_hash\_\_
    * All numeric operation will return a Word object, and there might be over flow problems.

1. Word
Word is similar to Byte as an class object. An Word object can be created by combining two 
Byte object, one for most significant Byte and one for least significant Byte. 
    * Attributes in Word:
        * _word: stores the value, ranging from 0x00 to 0xFFFF.
        * _lsb: Byte object, pointing to Byte._bytes[self._word & 0xFF]
        * _msb: Byte object, pointing to Byte._bytes[self._word >> 8]
        * _hex: stores 4 hexadecimal digits, from 0000 to FFFF
    * Just like \_bytes in Byte, there's also a \_words list stores the Word singletons, and 
this list is used in Byte.word() function and assigning \_word in Byte.
