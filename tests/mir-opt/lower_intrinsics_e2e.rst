tests/mir-opt/lower_intrinsics_e2e.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks that we do not have any branches in the MIR for the two tested functions.

// compile-flags: -Cpanic=abort
#![feature(core_intrinsics)]
#![crate_type = "lib"]

// EMIT_MIR lower_intrinsics_e2e.f_unit.PreCodegen.after.mir
pub fn f_unit() {
    f_dispatch(());
}


// EMIT_MIR lower_intrinsics_e2e.f_u64.PreCodegen.after.mir
pub fn f_u64() {
    f_dispatch(0u64);
}

#[inline(always)]
pub fn f_dispatch<T>(t: T) {
    if std::mem::size_of::<T>() == 0 {
        f_zst(t);
    } else {
        f_non_zst(t);
    }
}

#[inline(never)]
pub fn f_zst<T>(_t: T) {
}

#[inline(never)]
pub fn f_non_zst<T>(_t: T) {}


