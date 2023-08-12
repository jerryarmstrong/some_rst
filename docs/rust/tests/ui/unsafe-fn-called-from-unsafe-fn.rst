tests/ui/unsafe-fn-called-from-unsafe-fn.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
//
// See also: ui/unsafe/unsafe-fn-called-from-safe.rs

// pretty-expanded FIXME #23616

unsafe fn f() { return; }

unsafe fn g() {
    f();
}

pub fn main() {
    return;
}


