tests/ui/static/static-mut-bad-types.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static mut a: isize = 3;

fn main() {
    unsafe {
        a = true; //~ ERROR: mismatched types
    }
}


