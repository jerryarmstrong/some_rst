tests/mir-opt/const_prop/ref_deref_project.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zmir-enable-passes=-SimplifyLocals-before-const-prop
// EMIT_MIR ref_deref_project.main.PromoteTemps.diff
// EMIT_MIR ref_deref_project.main.ConstProp.diff

fn main() {
    *(&(4, 5).1); // This does not currently propagate (#67862)
}


