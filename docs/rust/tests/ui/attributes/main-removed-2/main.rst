tests/ui/attributes/main-removed-2/main.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:tokyo.rs
// compile-flags:--extern tokyo
// edition:2021

use tokyo::main;

#[main]
fn main() {
    panic!("the #[main] macro should replace this with non-panicking code")
}


