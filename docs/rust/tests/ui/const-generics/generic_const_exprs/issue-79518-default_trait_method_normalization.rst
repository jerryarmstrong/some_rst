tests/ui/const-generics/generic_const_exprs/issue-79518-default_trait_method_normalization.rs
=============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

// This test is a minimized reproduction for #79518 where
// during error handling for the type mismatch we would try
// to evaluate std::mem::size_of::<Self::Assoc> causing an ICE

trait Foo {
    type Assoc: PartialEq;
    const AssocInstance: Self::Assoc;

    fn foo()
    where
        [(); std::mem::size_of::<Self::Assoc>()]: ,
    {
        Self::AssocInstance == [(); std::mem::size_of::<Self::Assoc>()];
        //~^ Error: mismatched types
    }
}

fn main() {}


