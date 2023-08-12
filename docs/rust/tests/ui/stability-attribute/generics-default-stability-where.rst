tests/ui/stability-attribute/generics-default-stability-where.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:unstable_generic_param.rs

extern crate unstable_generic_param;

use unstable_generic_param::*;

impl<T> Trait3<usize> for T where T: Trait2<usize> { //~ ERROR use of unstable library feature 'unstable_default'
    fn foo() -> usize { T::foo() }
}

fn main() {}


