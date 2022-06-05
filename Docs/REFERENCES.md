
# References of conduct, creation and code usage on PxF

## Class Attributes
___
### Usage of `__slots__`
___
Slots are used to create variables at class creation time with a direct
reference avoiding the creation of the dynamic `__dict__` attribute,
which saves some memory and avoids lookup of variables, gaining some
speed.

To understand the usage and how it works completely, watch [mCoding \__slots__ video](https://www.youtube.com/watch?v=Iwf17zsDAnY)

---
### Usage of <something>
___
