tests/ui/macros/unreachable-macro-panic.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:internal error: entered unreachable code
// ignore-emscripten no processes

fn main() {
    unreachable!()
}


