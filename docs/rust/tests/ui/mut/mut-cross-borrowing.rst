tests/ui/mut/mut-cross-borrowing.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f(_: &mut isize) {}

fn main() {

    let mut x: Box<_> = Box::new(3);

    f(x)    //~ ERROR mismatched types
}


