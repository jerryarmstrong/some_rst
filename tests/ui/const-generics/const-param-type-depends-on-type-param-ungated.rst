tests/ui/const-generics/const-param-type-depends-on-type-param-ungated.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zsave-analysis
// Regression test for #69414 ^

use std::marker::PhantomData;

struct B<T, const N: T>(PhantomData<[T; N]>);
//~^ ERROR the type of const parameters must not depend on other generic parameters

fn main() {}


