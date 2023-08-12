tests/ui/panics/panic-set-handler.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:greetings from the panic handler
// ignore-emscripten no processes

use std::panic;

fn main() {
    panic::set_hook(Box::new(|i| {
        eprintln!("greetings from the panic handler");
    }));
    panic!("foobar");
}


