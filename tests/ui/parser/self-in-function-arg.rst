tests/ui/parser/self-in-function-arg.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x:i32, self: i32) -> i32 { self } //~ ERROR unexpected `self` parameter in function

fn main() {}


