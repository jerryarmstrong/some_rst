tests/ui/bare-static-string.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x: &'static str = "foo";
    println!("{}", x);
}


