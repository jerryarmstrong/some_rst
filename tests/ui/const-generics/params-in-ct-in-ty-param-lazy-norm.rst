tests/ui/const-generics/params-in-ct-in-ty-param-lazy-norm.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: full min
#![cfg_attr(full, feature(generic_const_exprs))]
#![cfg_attr(full, allow(incomplete_features))]

struct Foo<T, U = [u8; std::mem::size_of::<T>()]>(T, U);
//[min]~^ ERROR generic parameters may not be used in const operations

struct Bar<T = [u8; N], const N: usize>(T);
//~^ ERROR generic parameters with a default cannot use forward declared identifiers
//~| ERROR generic parameters with a default

fn main() {}


