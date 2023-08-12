tests/ui/consts/issue-79137-monomorphic.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Verify that variant count intrinsic can still evaluate for types like `Option<T>`.

#![feature(variant_count)]

pub struct GetVariantCount<T>(T);

impl<T> GetVariantCount<T> {
    pub const VALUE: usize = std::mem::variant_count::<T>();
}

const fn check_variant_count<T>() -> bool {
    matches!(GetVariantCount::<Option<T>>::VALUE, GetVariantCount::<Option<()>>::VALUE)
}

fn main() {
    assert!(check_variant_count::<()>());
}


