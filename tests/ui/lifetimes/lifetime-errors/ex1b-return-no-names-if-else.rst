tests/ui/lifetimes/lifetime-errors/ex1b-return-no-names-if-else.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x: &i32, y: &i32) -> &i32 { //~ ERROR missing lifetime
    if x > y { x } else { y }
}

fn main() {}


