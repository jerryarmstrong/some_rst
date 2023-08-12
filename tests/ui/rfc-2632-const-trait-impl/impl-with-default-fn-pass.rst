tests/ui/rfc-2632-const-trait-impl/impl-with-default-fn-pass.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(const_trait_impl)]

#[const_trait]
trait Tr {
    fn req(&self);

    fn default() {}
}

impl const Tr for u8 {
    fn req(&self) {}
}

macro_rules! impl_tr {
    ($ty: ty) => {
        impl const Tr for $ty {
            fn req(&self) {}
        }
    }
}

impl_tr!(u64);

fn main() {}


