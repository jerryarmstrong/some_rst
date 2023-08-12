tests/ui/unused-crate-deps/test-use-ok.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test-only use OK

// edition:2018
// check-pass
// aux-crate:bar=bar.rs
// compile-flags:--test

#![deny(unused_crate_dependencies)]

fn main() {}

#[test]
fn test_bar() {
    assert_eq!(bar::BAR, "bar");
}


