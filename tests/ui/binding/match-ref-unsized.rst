tests/ui/binding/match-ref-unsized.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Binding unsized expressions to ref patterns

pub fn main() {
    let ref a = *"abcdef";
    assert_eq!(a, "abcdef");

    match *"12345" {
        ref b => { assert_eq!(b, "12345") }
    }
}


