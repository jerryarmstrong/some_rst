tests/ui/binding/range-inclusive-pattern-precedence.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(box_patterns)]

const VALUE: usize = 21;

pub fn main() {
    match &18 {
        &(18..=18) => {}
        _ => { unreachable!(); }
    }
    match &21 {
        &(VALUE..=VALUE) => {}
        _ => { unreachable!(); }
    }
    match Box::new(18) {
        box (18..=18) => {}
        _ => { unreachable!(); }
    }
    match Box::new(21) {
        box (VALUE..=VALUE) => {}
        _ => { unreachable!(); }
    }
}


