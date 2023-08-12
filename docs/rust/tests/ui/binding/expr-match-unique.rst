tests/ui/binding/expr-match-unique.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Tests for match as expressions resulting in boxed types
fn test_box() {
    let res: Box<_> = match true { true => { Box::new(100) }, _ => panic!() };
    assert_eq!(*res, 100);
}

pub fn main() { test_box(); }


