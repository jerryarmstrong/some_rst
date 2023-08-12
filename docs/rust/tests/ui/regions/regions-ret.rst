tests/ui/regions/regions-ret.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn id<T>(x: T) -> T { x }

fn f(_x: &isize) -> &isize {
    return &id(3); //~ ERROR cannot return reference to temporary value
}

fn main() {
}


