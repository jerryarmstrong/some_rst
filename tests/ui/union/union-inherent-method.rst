tests/ui/union/union-inherent-method.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

union U {
    a: u8,
}

impl U {
    fn method(&self) -> u8 { unsafe { self.a } }
}

fn main() {
    let u = U { a: 10 };
    assert_eq!(u.method(), 10);
}


