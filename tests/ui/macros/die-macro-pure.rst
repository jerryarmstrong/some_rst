tests/ui/macros/die-macro-pure.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:test
// ignore-emscripten no processes

fn f() {
    panic!("test");
}

fn main() {
    f();
}


