tests/ui/unsafe-fn-called-from-unsafe-blk.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
//
// See also: ui/unsafe/unsafe-fn-called-from-safe.rs

// pretty-expanded FIXME #23616

unsafe fn f() { return; }

fn g() {
    unsafe {
        f();
    }
}

pub fn main() {
}


