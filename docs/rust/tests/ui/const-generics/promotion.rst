tests/ui/const-generics/promotion.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// tests that promoting expressions containing const parameters is allowed.
fn promotion_test<const N: usize>() -> &'static usize {
    &(3 + N)
}

fn main() {
    assert_eq!(promotion_test::<13>(), &16);
}


