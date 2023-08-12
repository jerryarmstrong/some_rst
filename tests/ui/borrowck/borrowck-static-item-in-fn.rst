tests/ui/borrowck/borrowck-static-item-in-fn.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Regression test for issue #7740

// pretty-expanded FIXME #23616

pub fn main() {
    static A: &'static char = &'A';
}


