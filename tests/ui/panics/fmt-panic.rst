tests/ui/panics/fmt-panic.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:meh
// ignore-emscripten no processes

fn main() {
    let str_var: String = "meh".to_string();
    panic!("{}", str_var);
}


