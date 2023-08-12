tests/ui/macros/macro-stmt_macro_in_expr_macro.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
macro_rules! foo {
    () => {
        struct Bar;
        struct Baz;
    }
}

macro_rules! grault {
    () => {{
        foo!();
        struct Xyzzy;
        0
    }}
}

fn main() {
    let x = grault!();
    assert_eq!(x, 0);
}


