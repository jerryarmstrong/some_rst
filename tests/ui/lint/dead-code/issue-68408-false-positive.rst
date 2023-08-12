tests/ui/lint/dead-code/issue-68408-false-positive.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Make sure we don't have any false positives here.

#![deny(dead_code)]

enum X {
    A { _a: () },
    B { _b: () },
}
impl X {
    fn a() -> X {
        X::A { _a: () }
    }
    fn b() -> Self {
        Self::B { _b: () }
    }
}

fn main() {
    let (_, _) = (X::a(), X::b());
}


