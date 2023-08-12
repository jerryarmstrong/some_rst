tests/mir-opt/fn_ptr_shim.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zmir-opt-level=0

// Tests that the `<fn() as Fn>` shim does not create a `Call` terminator with a `Self` callee
// (as only `FnDef` and `FnPtr` callees are allowed in MIR).

// EMIT_MIR core.ops-function-Fn-call.AddMovesForPackedDrops.before.mir
fn main() {
    call(noop as fn());
}

fn noop() {}

fn call<F: Fn()>(f: F) {
    f();
}


