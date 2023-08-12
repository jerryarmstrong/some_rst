tests/ui/const_prop/ice-assert-fail-div-by-zero.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// need to emit MIR, because const prop (which emits `unconditional_panic`) only runs if
// the `optimized_mir` query is run, which it isn't in check-only mode.
// compile-flags: --crate-type lib --emit=mir,link

#![warn(unconditional_panic)]

pub struct Fixed64(i64);

// HACK: this test passes only because this is a const fn that is written to metadata
pub const fn div(f: Fixed64) {
    f.0 / 0; //~ WARN will panic at runtime
}


