library/core/src/ffi/c_short.md
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    Equivalent to C's `signed short` (`short`) type.

This type will almost always be [`i16`], but may differ on some esoteric systems. The C standard technically only requires that this type be a signed integer with at least 16 bits; some systems may define it as `i32`, for example.

[`char`]: c_char


