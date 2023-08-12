tests/mir-opt/const_prop/ref_deref.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zmir-enable-passes=-SimplifyLocals-before-const-prop
// EMIT_MIR ref_deref.main.PromoteTemps.diff
// EMIT_MIR ref_deref.main.ConstProp.diff

fn main() {
    *(&4);
}


