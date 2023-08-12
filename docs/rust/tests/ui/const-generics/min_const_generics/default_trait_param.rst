tests/ui/const-generics/min_const_generics/default_trait_param.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
trait Foo<const KIND: bool = true> {}

fn main() {}


