tests/mir-opt/const_prop/switch_int.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[inline(never)]
fn foo(_: i32) { }

// EMIT_MIR switch_int.main.ConstProp.diff
// EMIT_MIR switch_int.main.SimplifyConstCondition-after-const-prop.diff
fn main() {
    match 1 {
        1 => foo(0),
        _ => foo(-1),
    }
}


