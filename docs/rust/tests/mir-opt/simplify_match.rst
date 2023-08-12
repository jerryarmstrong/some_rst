tests/mir-opt/simplify_match.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[inline(never)]
fn noop() {}

// EMIT_MIR simplify_match.main.ConstProp.diff
fn main() {
    match { let x = false; x } {
        true => noop(),
        false => {},
    }
}


