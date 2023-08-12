tests/ui/const-generics/defaults/param-order-err-pretty-prints-default.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<const M: usize = 10, 'a>(&'a u32);
//~^ ERROR lifetime parameters must be declared prior to type and const parameters

fn main() {}


