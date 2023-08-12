tests/ui/union/union-trait-impl.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

use std::fmt;

union U {
    a: u8
}

impl fmt::Display for U {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        unsafe { write!(f, "Oh hai {}", self.a) }
    }
}

fn main() {
    assert_eq!(U { a: 2 }.to_string(), "Oh hai 2");
}


