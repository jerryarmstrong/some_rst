tests/ui/rfc-1937-termination-trait/termination-trait-for-never.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:oh, dear
// ignore-emscripten no processes

fn main() -> ! {
    panic!("oh, dear");
}


