tests/ui/expr/if/if-check-panic.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:Number is odd
// ignore-emscripten no processes

fn even(x: usize) -> bool {
    if x < 2 {
        return false;
    } else if x == 2 {
        return true;
    } else {
        return even(x - 2);
    }
}

fn foo(x: usize) {
    if even(x) {
        println!("{}", x);
    } else {
        panic!("Number is odd");
    }
}

fn main() {
    foo(3);
}


