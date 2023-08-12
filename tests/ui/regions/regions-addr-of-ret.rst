tests/ui/regions/regions-addr-of-ret.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn f(x: &isize) -> &isize {
    return &*x;
}

pub fn main() {
    let three = &3;
    println!("{}", *f(three));
}


