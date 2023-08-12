tests/mir-opt/simplify_locals_fixedpoint.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zmir-opt-level=1

fn foo<T>() {
    if let (Some(a), None) = (Option::<u8>::None, Option::<T>::None) {
        if a > 42u8 {

        }
    }
}

fn main() {
    foo::<()>();
}

// EMIT_MIR simplify_locals_fixedpoint.foo.SimplifyLocals-final.diff


