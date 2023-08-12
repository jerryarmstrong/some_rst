tests/ui/unsized-locals/simple-unsized-locals.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(incomplete_features)]
#![feature(unsized_locals)]

fn main() {
    let foo: Box<[u8]> = Box::new(*b"foo");
    let _foo: [u8] = *foo;
}


