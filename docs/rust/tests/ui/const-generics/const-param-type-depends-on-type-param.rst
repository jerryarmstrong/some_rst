tests/ui/const-generics/const-param-type-depends-on-type-param.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: full min

#![cfg_attr(full, feature(adt_const_params))]
#![cfg_attr(full, allow(incomplete_features))]

// Currently, const parameters cannot depend on other generic parameters,
// as our current implementation can't really support this.
//
// We may want to lift this restriction in the future.

pub struct Dependent<T, const X: T>([(); X]);
//~^ ERROR: the type of const parameters must not depend on other generic parameters
//~| ERROR: parameter `T` is never used

fn main() {}


