tests/ui/closures/diverging-closure.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:oops
// ignore-emscripten no processes

fn main() {
    let func = || -> ! {
        panic!("oops");
    };
    func();
}


