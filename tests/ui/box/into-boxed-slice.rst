tests/ui/box/into-boxed-slice.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(box_into_boxed_slice)]

use std::boxed::Box;
fn main() {
    assert_eq!(Box::into_boxed_slice(Box::new(5u8)), Box::new([5u8]) as Box<[u8]>);
    assert_eq!(Box::into_boxed_slice(Box::new([25u8])), Box::new([[25u8]]) as Box<[[u8; 1]]>);
    let a: Box<[Box<[u8; 1]>]> = Box::into_boxed_slice(Box::new(Box::new([5u8])));
    let b: Box<[Box<[u8; 1]>]> = Box::new([Box::new([5u8])]);
    assert_eq!(a, b);
}


