tests/ui/print_type_sizes/anonymous.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z print-type-sizes
// build-pass

// All of the types that occur in this function are uninteresting, in
// that one cannot control the sizes of these types with the same sort
// of enum-variant manipulation tricks.

#![feature(start)]

#[start]
fn start(_: isize, _: *const *const u8) -> isize {
    let _byte: u8 = 0;
    let _word: usize = 0;
    let _tuple: (u8, usize)= (0, 0);
    let _array: [u8; 128] = [0; 128];
    let _fn: fn (u8) -> u8 = id;
    let _diverging: fn (u8) -> ! = bye;

    fn id(x: u8) -> u8 { x };
    fn bye(_: u8) -> ! { loop { } }

    0
}


