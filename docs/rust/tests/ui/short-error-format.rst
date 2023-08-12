tests/ui/short-error-format.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --error-format=short

fn foo(_: u32) {}

fn main() {
    foo("Bonjour".to_owned());
    let x = 0u32;
    x.salut();
}


