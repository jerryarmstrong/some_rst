tests/ui/borrowck/borrowck-assign-to-constants.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static foo: isize = 5;

fn main() {
    // assigning to various global constants
    foo = 6; //~ ERROR cannot assign to immutable static item `foo`
}


