tests/ui/mod-subitem-as-enum-variant.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod Mod {
    pub struct FakeVariant<T>(pub T);
}

fn main() {
    Mod::FakeVariant::<i32>(0);
    Mod::<i32>::FakeVariant(0);
    //~^ ERROR type arguments are not allowed on module `Mod` [E0109]
}


