tests/ui/const-generics/const-fn-with-const-param.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks that `const fn` with const params can be used.
// run-pass

const fn const_u32_identity<const X: u32>() -> u32 {
    X
}

fn main() {
    assert_eq!(const_u32_identity::<18>(), 18);
}


