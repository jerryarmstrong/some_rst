tests/ui/rfc-1937-termination-trait/termination-trait-for-str.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern: An error message for you
// failure-status: 1
// ignore-emscripten no processes

fn main() -> Result<(), &'static str> {
    Err("An error message for you")
}


