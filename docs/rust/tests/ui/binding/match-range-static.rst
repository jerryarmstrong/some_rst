tests/ui/binding/match-range-static.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616
#![allow(non_upper_case_globals)]

const s: isize = 1;
const e: isize = 42;

pub fn main() {
    match 7 {
        s..=e => (),
        _ => (),
    }
}


