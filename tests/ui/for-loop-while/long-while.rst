tests/ui/for-loop-while/long-while.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#![allow(unused_variables)]

pub fn main() {
    let mut i: isize = 0;
    while i < 1000000 {
        i += 1;
        let x = 3;
    }
}


