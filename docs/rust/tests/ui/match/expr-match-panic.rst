tests/ui/match/expr-match-panic.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:explicit panic
// ignore-emscripten no processes

fn main() {
    let _x = match true {
        false => 0,
        true => panic!(),
    };
}


