tests/ui/consts/issue-70942-trait-vs-impl-mismatch.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Nat {
    const VALUE: usize;
}

struct Zero;

impl Nat for Zero {
    const VALUE: i32 = 0;
    //~^ ERROR implemented const `VALUE` has an incompatible type for trait
}

fn main() {
    let _: [i32; Zero::VALUE] = [];
}


