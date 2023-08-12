tests/ui/unique/unique-generic-assign.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Issue #976


// pretty-expanded FIXME #23616

fn f<T>(x: Box<T>) {
    let _x2 = x;
}
pub fn main() { }


