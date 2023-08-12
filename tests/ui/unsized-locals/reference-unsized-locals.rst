tests/ui/unsized-locals/reference-unsized-locals.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(incomplete_features)]
#![feature(unsized_locals)]

fn main() {
    let foo: Box<[u8]> = Box::new(*b"foo");
    let foo: [u8] = *foo;
    assert_eq!(&foo, b"foo" as &[u8]);
}


