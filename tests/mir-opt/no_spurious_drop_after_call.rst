tests/mir-opt/no_spurious_drop_after_call.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-wasm32-bare compiled with panic=abort by default

// Test that after the call to `std::mem::drop` we do not generate a
// MIR drop of the argument. (We used to have a `DROP(_2)` in the code
// below, as part of bb3.)

// EMIT_MIR no_spurious_drop_after_call.main.ElaborateDrops.before.mir
fn main() {
    std::mem::drop("".to_string());
}


