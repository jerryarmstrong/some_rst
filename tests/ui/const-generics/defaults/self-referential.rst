tests/ui/const-generics/defaults/self-referential.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo<const M: u8, const M: u8 = M> {}
//~^ ERROR the name `M` is already used for a generic parameter in this item's generic parameters
impl Foo<2> for () {}
fn main() {}


