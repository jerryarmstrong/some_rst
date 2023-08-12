tests/ui/borrowck/immutable-arg.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(_x: u32) {
    _x = 4;
    //~^ ERROR cannot assign to immutable argument `_x`
}

fn main() {}


