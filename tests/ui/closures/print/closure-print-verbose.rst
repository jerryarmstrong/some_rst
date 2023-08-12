tests/ui/closures/print/closure-print-verbose.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zverbose

// Same as closure-coerce-fn-1.rs

// Ensure that capturing closures are never coerced to fns
// Especially interesting as non-capturing closures can be.

fn main() {
    let mut a = 0u8;
    let foo: fn(u8) -> u8 = |v: u8| { a += v; a };
    //~^ ERROR mismatched types
}


