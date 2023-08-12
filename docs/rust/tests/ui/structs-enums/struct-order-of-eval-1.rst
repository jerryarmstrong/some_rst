tests/ui/structs-enums/struct-order-of-eval-1.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

struct S { f0: String, f1: isize }

pub fn main() {
    let s = "Hello, world!".to_string();
    let s = S {
        f0: s.to_string(),
        ..S {
            f0: s,
            f1: 23
        }
    };
    assert_eq!(s.f0, "Hello, world!");
}


