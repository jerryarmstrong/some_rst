tests/ui/feature-gates/feature-gate-yeet_expr.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition 2018

pub fn demo() -> Option<i32> {
    do yeet //~ ERROR `do yeet` expression is experimental
}

pub fn main() -> Result<(), String> {
    do yeet "hello"; //~ ERROR `do yeet` expression is experimental
}


