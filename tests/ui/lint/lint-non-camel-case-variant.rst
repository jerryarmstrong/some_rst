tests/ui/lint/lint-non-camel-case-variant.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(non_camel_case_types)]

pub enum Foo {
    #[allow(non_camel_case_types)]
    bar
}

fn main() {}


