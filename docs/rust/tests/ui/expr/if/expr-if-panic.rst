tests/ui/expr/if/expr-if-panic.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:explicit panic
// ignore-emscripten no processes

fn main() {
    let _x = if false {
        0
    } else if true {
        panic!()
    } else {
        10
    };
}


