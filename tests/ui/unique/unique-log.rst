tests/ui/unique/unique-log.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let i: Box<_> = Box::new(100);
    println!("{}", i);
}


