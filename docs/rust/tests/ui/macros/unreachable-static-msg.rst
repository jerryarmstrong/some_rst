tests/ui/macros/unreachable-static-msg.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:internal error: entered unreachable code: uhoh
// ignore-emscripten no processes

fn main() {
    unreachable!("uhoh")
}


