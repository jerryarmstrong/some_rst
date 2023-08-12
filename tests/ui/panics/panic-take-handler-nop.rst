tests/ui/panics/panic-take-handler-nop.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:thread 'main' panicked at 'foobar'
// ignore-emscripten no processes

use std::panic;

fn main() {
    panic::take_hook();
    panic!("foobar");
}


