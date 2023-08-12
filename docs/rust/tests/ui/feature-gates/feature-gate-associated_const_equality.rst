tests/ui/feature-gates/feature-gate-associated_const_equality.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait TraitWAssocConst {
  const A: usize;
}
pub struct Demo {}

impl TraitWAssocConst for Demo {
  const A: usize = 32;
}

fn foo<A: TraitWAssocConst<A=32>>() {}
//~^ ERROR associated const equality

fn main() {
  foo::<Demo>();
}


