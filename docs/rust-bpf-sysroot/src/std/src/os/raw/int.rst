src/std/src/os/raw/int.md
=========================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: md

    Equivalent to C's `signed int` (`int`) type.

This type will almost always be [`i32`], but may differ on some esoteric systems. The C standard technically only requires that this type be a signed integer that is at least the size of a [`short`]; some systems define it as an [`i16`], for example.

[`short`]: c_short


