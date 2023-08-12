tests/ui/consts/const-repeated-values.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
const FOO: isize = 42;

enum Bar {
    Boo = *[&FOO; 4][3],
}

fn main() {
    assert_eq!(Bar::Boo as isize, 42);
}


