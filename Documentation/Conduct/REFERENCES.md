# Code conduct
When writing new code or using functions that exist, there
are some conducts we can take to make code better
and faster


## Creation of code
### Imports
#### Styling
When importing modules or objects, the structure follows:
```python
# Standard Imports

# Embedder imports

# External Imports

## External imports
```
The reason for this division style of imports its so that when
identifying which imports belong to which sources, it is easier
to identify.

For example, if we import an external module called `foo`,
the best way to know where `foo` is coming from first glance is
to see that it is under external imports, like:
```python
## External imports
import foo
```


### Class Attributes
#### Usage of `__slots__`
Slots are used to create variables at class creation time with a direct
reference avoiding the creation of the dynamic `__dict__` attribute,
which saves some memory and avoids lookup of variables, gaining some
speed.

To understand the usage and how it works completely, watch [mCoding's \__slots\__ video](https://www.youtube.com/watch?v=Iwf17zsDAnY)


## Usage of code
Nothing to reference, for now.
