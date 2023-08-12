tests/mir-opt/derefer_complex_case.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: Derefer
// EMIT_MIR derefer_complex_case.main.Derefer.diff
// ignore-wasm32

fn main() {
    for &foo in &[42, 43] { drop(foo) }
}


