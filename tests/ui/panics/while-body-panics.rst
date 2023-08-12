tests/ui/panics/while-body-panics.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(while_true)]

// run-fail
// error-pattern:quux
// ignore-emscripten no processes

fn main() {
    let _x: isize = {
        while true {
            panic!("quux");
        }
        8
    };
}


