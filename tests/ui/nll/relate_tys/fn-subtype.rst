tests/ui/nll/relate_tys/fn-subtype.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that NLL produces correct spans for higher-ranked subtyping errors.
//
// compile-flags:-Zno-leak-check

fn main() {
    let x: fn(&'static ()) = |_| {};
    let y: for<'a> fn(&'a ()) = x; //~ ERROR mismatched types [E0308]
}


