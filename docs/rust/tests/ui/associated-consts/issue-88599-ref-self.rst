tests/ui/associated-consts/issue-88599-ref-self.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

pub trait First {
    const CONST: usize;
}
pub trait Second {}

impl<'a> First for dyn Second
where
    &'a Self: First,
{
    const CONST: usize = <&Self>::CONST;
}

trait Third: First
where
    [u8; Self::CONST]:
{
    const VAL: [u8; Self::CONST] = [0; Self::CONST];
}

fn main() {}


