tests/ui/panics/result-get-panic.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:called `Result::unwrap()` on an `Err` value
// ignore-emscripten no processes

use std::result::Result::Err;

fn main() {
    println!("{}", Err::<isize, String>("kitty".to_string()).unwrap());
}


