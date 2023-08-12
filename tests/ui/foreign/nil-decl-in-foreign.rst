tests/ui/foreign/nil-decl-in-foreign.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(improper_ctypes)]
#![allow(dead_code)]
// Issue #901
// pretty-expanded FIXME #23616

mod libc {
    extern "C" {
        pub fn printf(x: ());
    }
}

pub fn main() {}


