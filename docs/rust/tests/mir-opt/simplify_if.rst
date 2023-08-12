tests/mir-opt/simplify_if.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[inline(never)]
fn noop() {}

// EMIT_MIR simplify_if.main.SimplifyConstCondition-after-const-prop.diff
fn main() {
    if false {
        noop();
    }
}


