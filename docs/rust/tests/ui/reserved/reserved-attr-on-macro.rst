tests/ui/reserved/reserved-attr-on-macro.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[rustc_attribute_should_be_reserved]
//~^ ERROR cannot find attribute `rustc_attribute_should_be_reserved` in this scope
//~| ERROR attributes starting with `rustc` are reserved for use by the `rustc` compiler

macro_rules! foo {
    () => (());
}

fn main() {
    foo!(); //~ ERROR cannot determine resolution for the macro `foo`
}


