src/tools/clippy/tests/ui-toml/struct_excessive_bools/test.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::struct_excessive_bools)]

struct S {
    a: bool,
}

struct Foo;

fn main() {}


