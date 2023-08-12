tests/ui/const-generics/const-param-type-depends-on-const-param.rs
==================================================================

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

pub struct Dependent<const N: usize, const X: [u8; N]>([(); N]);
//~^ ERROR: the type of const parameters must not depend on other generic parameters
//[min]~^^ ERROR `[u8; N]` is forbidden

pub struct SelfDependent<const N: [u8; N]>;
//~^ ERROR: the type of const parameters must not depend on other generic parameters
//[min]~^^ ERROR `[u8; N]` is forbidden

fn main() {}


