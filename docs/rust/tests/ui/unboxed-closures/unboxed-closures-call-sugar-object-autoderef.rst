tests/ui/unboxed-closures/unboxed-closures-call-sugar-object-autoderef.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that the call operator autoderefs when calling to an object type.

use std::ops::FnMut;

fn make_adder(x: isize) -> Box<dyn FnMut(isize)->isize + 'static> {
    Box::new(move |y| { x + y })
}

pub fn main() {
    let mut adder = make_adder(3);
    let z = adder(2);
    println!("{}", z);
    assert_eq!(z, 5);
}


