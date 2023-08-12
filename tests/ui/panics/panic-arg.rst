tests/ui/panics/panic-arg.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:woe
// ignore-emscripten no processes

fn f(a: isize) {
    println!("{}", a);
}

fn main() {
    f(panic!("woe"));
}


