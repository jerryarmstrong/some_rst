tests/ui/const-generics/apit-with-const-param.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Trait {}

fn f<const N: usize>(_: impl Trait) {}

fn main() {}


