tests/ui/match/expr-match-panic-fn.rs
=====================================

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
    let x = match true {
        true => f(),
        false => 10,
    };
    return x;
}

fn main() {
    g();
}


