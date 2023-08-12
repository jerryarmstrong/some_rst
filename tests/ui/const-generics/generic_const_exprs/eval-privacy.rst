tests/ui/const-generics/generic_const_exprs/eval-privacy.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

pub struct Const<const U: u8>;

pub trait Trait {
    type AssocTy;
    fn assoc_fn() -> Self::AssocTy;
}

impl<const U: u8> Trait for Const<U> // OK, trait impl predicates
where
    Const<{ my_const_fn(U) }>: ,
{
    type AssocTy = Const<{ my_const_fn(U) }>;
    //~^ ERROR private type
    fn assoc_fn() -> Self::AssocTy {
        Const
    }
}

const fn my_const_fn(val: u8) -> u8 {
    // body of this function doesn't matter
    val
}


