tests/ui/fn/expr-fn-panic.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:explicit panic
// ignore-emscripten no processes

fn f() -> ! {
    panic!()
}

fn main() {
    f();
}


