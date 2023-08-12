tests/ui/expr/if/expr-if-panic-fn.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:explicit panic
// ignore-emscripten no processes

fn f() -> ! {
    panic!()
}

fn g() -> isize {
    let x = if true {
        f()
    } else {
        10
    };
    return x;
}

fn main() {
    g();
}


