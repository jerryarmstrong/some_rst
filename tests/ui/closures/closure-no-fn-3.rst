tests/ui/closures/closure-no-fn-3.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Ensure that capturing closures are never coerced to fns
// Especially interesting as non-capturing closures can be.

fn main() {
    let b = 0u8;
    let baz: fn() -> u8 = (|| { b }) as fn() -> u8;
    //~^ ERROR non-primitive cast
}


