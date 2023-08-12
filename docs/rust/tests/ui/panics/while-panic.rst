tests/ui/panics/while-panic.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(while_true)]

// run-fail
// error-pattern:giraffe
// ignore-emscripten no processes

fn main() {
    panic!("{}", {
        while true {
            panic!("giraffe")
        }
        "clandestine"
    });
}


