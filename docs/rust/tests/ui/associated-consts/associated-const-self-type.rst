tests/ui/associated-consts/associated-const-self-type.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait MyInt {
    const ONE: Self;
}

impl MyInt for i32 {
    const ONE: i32 = 1;
}

fn main() {
    assert_eq!(1, <i32>::ONE);
}


