tests/mir-opt/derefer_terminator_test.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: Derefer
// EMIT_MIR derefer_terminator_test.main.Derefer.diff
// ignore-wasm32

fn main() {
    let b = foo();
    let d = foo();
    match ****(&&&&b) {
        true => {let x = 5;},
        false => {}
    }
    let y = 42;
}

fn foo() -> bool {
    true
}


