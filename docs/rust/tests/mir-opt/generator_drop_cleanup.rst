tests/mir-opt/generator_drop_cleanup.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators, generator_trait)]

// ignore-wasm32-bare compiled with panic=abort by default

// Regression test for #58892, generator drop shims should not have blocks
// spuriously marked as cleanup

// EMIT_MIR generator_drop_cleanup.main-{closure#0}.generator_drop.0.mir
fn main() {
    let gen = || {
        let _s = String::new();
        yield;
    };
}


