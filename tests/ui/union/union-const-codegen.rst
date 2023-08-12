tests/ui/union/union-const-codegen.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

union U {
    a: u64,
    b: u64,
}

const C: U = U { b: 10 };

fn main() {
    unsafe {
        let a = C.a;
        let b = C.b;
        assert_eq!(a, 10);
        assert_eq!(b, 10);
     }
}


