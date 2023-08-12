tests/ui/log-poly.rs
====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(Debug)]
enum Numbers {
    Three
}

pub fn main() {
    println!("{:?}", 1);
    println!("{:?}", 2.0f64);
    println!("{:?}", Numbers::Three);
    println!("{:?}", vec![4]);
}


