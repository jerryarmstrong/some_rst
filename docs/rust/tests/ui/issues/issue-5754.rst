tests/ui/issues/issue-5754.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![allow(dead_code)]
#![allow(improper_ctypes)]

// pretty-expanded FIXME #23616

struct TwoDoubles {
    r: f64,
    i: f64
}

extern "C" {
    fn rust_dbg_extern_identity_TwoDoubles(arg1: TwoDoubles) -> TwoDoubles;
}

pub fn main() {}


