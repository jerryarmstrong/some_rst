tests/ui/auto-traits/auto-is-contextual.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(path_statements)]
#![allow(dead_code)]
macro_rules! auto {
    () => (struct S;)
}

auto!();

fn auto() {}

fn main() {
    auto();
    let auto = 10;
    auto;
    auto as u8;
}


