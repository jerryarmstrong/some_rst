tests/ui/lint/dead-code/unused-variant.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(dead_code)]

#[derive(Clone)]
enum Enum {
    Variant1, //~ ERROR: variant `Variant1` is never constructed
    Variant2,
}

fn main() {
    let e = Enum::Variant2;
    e.clone();
}


