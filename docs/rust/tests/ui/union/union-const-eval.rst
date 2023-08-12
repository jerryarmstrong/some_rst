tests/ui/union/union-const-eval.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

union U {
    a: usize,
    b: usize,
}

const C: U = U { a: 10 };

fn main() {
    let a: [u8; unsafe { C.a }];
    let b: [u8; unsafe { C.b }];
}


