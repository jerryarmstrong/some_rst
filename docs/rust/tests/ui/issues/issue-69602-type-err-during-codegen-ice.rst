tests/ui/issues/issue-69602-type-err-during-codegen-ice.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait TraitA {
    const VALUE: usize;
}

struct A;
impl TraitA for A {
  const VALUE: usize = 0;
}

trait TraitB {
    type MyA: TraitA;
    const VALUE: usize = Self::MyA::VALUE;
}

struct B;
impl TraitB for B { //~ ERROR not all trait items implemented, missing: `MyA`
    type M   = A; //~ ERROR type `M` is not a member of trait `TraitB`
}

fn main() {
    let _ = [0; B::VALUE];
    //~^ constant
}


