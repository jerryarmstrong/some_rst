tests/ui/consts/const-prop-ice2.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

fn main() {
    enum Enum { One=1 }
    let xs=[0;1 as usize];
    println!("{}", xs[Enum::One as usize]); //~ ERROR this operation will panic at runtime
}


