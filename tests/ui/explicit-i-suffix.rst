tests/ui/explicit-i-suffix.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_must_use)]
// pretty-expanded FIXME #23616

pub fn main() {
    let x: isize = 8;
    let y = 9;
    x + y;

    let q: isize = -8;
    let r = -9;
    q + r;
}


