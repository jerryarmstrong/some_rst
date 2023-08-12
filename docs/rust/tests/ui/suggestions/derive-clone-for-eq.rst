tests/ui/suggestions/derive-clone-for-eq.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// https://github.com/rust-lang/rust/issues/79076

use std::cmp::PartialEq;

#[derive(Clone, Eq)] //~ ERROR [E0277]
pub struct Struct<T>(T);

impl<T: Clone, U> PartialEq<U> for Struct<T>
where
    U: Into<Struct<T>> + Clone
{
    fn eq(&self, _other: &U) -> bool {
        todo!()
    }
}

fn main() {}


