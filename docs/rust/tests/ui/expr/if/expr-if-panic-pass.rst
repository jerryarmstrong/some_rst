tests/ui/expr/if/expr-if-panic-pass.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn test_if_panic() {
    let x = if false { panic!() } else { 10 };
    assert_eq!(x, 10);
}

fn test_else_panic() {
    let x = if true { 10 } else { panic!() };
    assert_eq!(x, 10);
}

fn test_elseif_panic() {
    let x = if false { 0 } else if false { panic!() } else { 10 };
    assert_eq!(x, 10);
}

pub fn main() { test_if_panic(); test_else_panic(); test_elseif_panic(); }


