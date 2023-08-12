tests/ui/const-generics/defaults/complex-generic-default-expr.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: full min
//[full] check-pass
#![cfg_attr(full, feature(generic_const_exprs))]
#![cfg_attr(full, allow(incomplete_features))]

struct Foo<const N: usize, const M: usize = { N + 1 }>;
//[min]~^ ERROR generic parameters may not be used in const operations

struct Bar<T, const TYPE_SIZE: usize = { std::mem::size_of::<T>() }>(T);
//[min]~^ ERROR generic parameters may not be used in const operations

fn main() {}


