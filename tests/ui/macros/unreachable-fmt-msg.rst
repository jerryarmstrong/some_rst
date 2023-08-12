tests/ui/macros/unreachable-fmt-msg.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:internal error: entered unreachable code: 6 is not prime
// ignore-emscripten no processes

fn main() {
    unreachable!("{} is not {}", 6u32, "prime");
}


