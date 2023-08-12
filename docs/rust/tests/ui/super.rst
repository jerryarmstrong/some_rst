tests/ui/super.rs
=================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// pretty-expanded FIXME #23616

pub mod a {
    pub fn f() {}
    pub mod b {
        fn g() {
            super::f();
        }
    }
}

pub fn main() {
}


