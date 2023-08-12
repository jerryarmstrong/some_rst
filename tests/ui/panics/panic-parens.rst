tests/ui/panics/panic-parens.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Fail macros without arguments need to be disambiguated in
// certain positions

// run-fail
// error-pattern:oops
// ignore-emscripten no processes

fn bigpanic() {
    while (panic!("oops")) {
        if (panic!()) {
            match (panic!()) {
                () => {}
            }
        }
    }
}

fn main() {
    bigpanic();
}


