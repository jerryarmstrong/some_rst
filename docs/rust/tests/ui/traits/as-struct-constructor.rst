tests/ui/traits/as-struct-constructor.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait TraitNotAStruct {}

fn main() {
    TraitNotAStruct{ value: 0 };
    //~^ ERROR expected struct, variant or union type, found trait `TraitNotAStruct`
}


