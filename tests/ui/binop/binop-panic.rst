tests/ui/binop/binop-panic.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:quux
// ignore-emscripten no processes

fn my_err(s: String) -> ! {
    println!("{}", s);
    panic!("quux");
}

fn main() {
    3_usize == my_err("bye".to_string());
}


