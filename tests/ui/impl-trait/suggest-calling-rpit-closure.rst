tests/ui/impl-trait/suggest-calling-rpit-closure.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn whatever() -> i32 {
    opaque()
//~^ ERROR mismatched types
}

fn opaque() -> impl Fn() -> i32 {
    || 0
}

fn main() {
    let _ = whatever();
}


