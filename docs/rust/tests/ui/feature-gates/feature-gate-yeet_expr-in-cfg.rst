tests/ui/feature-gates/feature-gate-yeet_expr-in-cfg.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition 2021

pub fn demo() -> Option<i32> {
    #[cfg(nope)]
    {
        do yeet //~ ERROR `do yeet` expression is experimental
    }

    Some(1)
}

#[cfg(nope)]
pub fn alternative() -> Result<(), String> {
    do yeet "hello"; //~ ERROR `do yeet` expression is experimental
}

fn main() {
    demo();
}


