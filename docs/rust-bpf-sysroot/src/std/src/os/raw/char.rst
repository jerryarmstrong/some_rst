src/std/src/os/raw/char.md
==========================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: md

    Equivalent to C's `char` type.

[C's `char` type] is completely unlike [Rust's `char` type]; while Rust's type represents a unicode scalar value, C's `char` type is just an ordinary integer. This type will always be either [`i8`] or [`u8`], as the type is defined as being one byte long.

C chars are most commonly used to make C strings. Unlike Rust, where the length of a string is included alongside the string, C strings mark the end of a string with the character `'\0'`. See [`CStr`] for more information.

[C's `char` type]: https://en.wikipedia.org/wiki/C_data_types#Basic_types
[Rust's `char` type]: char
[`CStr`]: crate::ffi::CStr


