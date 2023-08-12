tests/mir-opt/slice_drop_shim.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zmir-opt-level=0


// EMIT_MIR core.ptr-drop_in_place.[String].AddMovesForPackedDrops.before.mir
fn main() {
    let _fn = std::ptr::drop_in_place::<[String]> as unsafe fn(_);
}


