tests/ui/associated-type-bounds/missing-trait-bound-for-assoc-fails.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(dead_code)]
fn foo<M>(_m: M)
where
    M::Item: Temp,
    //~^ ERROR cannot find trait `Temp` in this scope [E0405]
    //~| ERROR associated type `Item` not found for `M` [E0220]
{
}

fn main() {}


