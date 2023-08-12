tests/ui/consts/issue-79137-toogeneric.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `variant_count` only gets evaluated once the type is concrete enough.

#![feature(variant_count)]

pub struct GetVariantCount<T>(T);

impl<T> GetVariantCount<T> {
    pub const VALUE: usize = std::mem::variant_count::<T>();
}

const fn check_variant_count<T>() -> bool {
    matches!(GetVariantCount::<T>::VALUE, GetVariantCount::<T>::VALUE)
    //~^ ERROR constant pattern depends on a generic parameter
    //~| ERROR constant pattern depends on a generic parameter
}

fn main() {
    assert!(check_variant_count::<Option<()>>());
}


