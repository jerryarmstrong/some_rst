tests/ui/borrowck/borrowck-local-borrow.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:panic 1
// ignore-emscripten no processes

fn main() {
    let x = 2;
    let y = &x;
    panic!("panic 1");
}


