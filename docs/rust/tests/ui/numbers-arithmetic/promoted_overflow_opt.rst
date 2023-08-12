tests/ui/numbers-arithmetic/promoted_overflow_opt.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// compile-flags: -O

fn main() {
    let x = &(0u32 - 1);
    assert_eq!(*x, u32::MAX)
}


