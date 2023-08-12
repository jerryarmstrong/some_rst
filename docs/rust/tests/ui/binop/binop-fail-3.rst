tests/ui/binop/binop-fail-3.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:quux
// ignore-emscripten no processes

fn foo() -> ! {
    panic!("quux");
}

fn main() {
    foo() == foo(); // these types wind up being defaulted to ()
}


