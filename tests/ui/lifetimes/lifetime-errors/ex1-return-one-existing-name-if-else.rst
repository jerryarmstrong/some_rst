tests/ui/lifetimes/lifetime-errors/ex1-return-one-existing-name-if-else.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<'a>(x: &'a i32, y: &i32) -> &'a i32 {
    if x > y { x } else { y } //~ ERROR explicit lifetime
}

fn main() { }


