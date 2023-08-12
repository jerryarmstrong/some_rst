tests/ui/traits/object/lifetime-first.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::fmt::Display;

static BYTE: u8 = 33;

fn main() {
    let x: &(dyn 'static + Display) = &BYTE;
    let y: Box<dyn 'static + Display> = Box::new(BYTE);
    let xstr = format!("{}", x);
    let ystr = format!("{}", y);
    assert_eq!(xstr, "33");
    assert_eq!(ystr, "33");
}


