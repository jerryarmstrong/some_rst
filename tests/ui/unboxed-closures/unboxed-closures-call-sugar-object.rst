tests/ui/unboxed-closures/unboxed-closures-call-sugar-object.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::ops::FnMut;

fn make_adder(x: isize) -> Box<dyn FnMut(isize)->isize + 'static> {
    Box::new(move |y| { x + y })
}

pub fn main() {
    let mut adder = make_adder(3);
    let z = (*adder)(2);
    println!("{}", z);
    assert_eq!(z, 5);
}


