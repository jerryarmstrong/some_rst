tests/ui/feature-gates/feature-gate-adt_const_params.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<const NAME: &'static str>; //~ ERROR `&'static str` is forbidden
fn main() {}


