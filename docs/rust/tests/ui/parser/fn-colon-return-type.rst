tests/ui/parser/fn-colon-return-type.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x: i32): i32 {
//~^ ERROR return types are denoted using `->`
    x
}

fn main() {}


