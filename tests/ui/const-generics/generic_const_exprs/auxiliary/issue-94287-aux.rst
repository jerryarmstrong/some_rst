tests/ui/const-generics/generic_const_exprs/auxiliary/issue-94287-aux.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]

use std::str::FromStr;

pub struct If<const CONDITION: bool>;

pub trait True {}

impl True for If<true> {}

pub struct FixedI32<const FRAC: u32>;

impl<const FRAC: u32> FromStr for FixedI32<FRAC>
where
    If<{ FRAC <= 32 }>: True,
{
    type Err = ();
    fn from_str(_s: &str) -> Result<Self, Self::Err> {
        unimplemented!()
    }
}


