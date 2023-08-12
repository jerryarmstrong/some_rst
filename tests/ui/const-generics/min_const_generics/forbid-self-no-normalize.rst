tests/ui/const-generics/min_const_generics/forbid-self-no-normalize.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait AlwaysApplicable {
    type Assoc;
}
impl<T: ?Sized> AlwaysApplicable for T {
    type Assoc = usize;
}

trait BindsParam<T> {
    type ArrayTy;
}
impl<T> BindsParam<T> for <T as AlwaysApplicable>::Assoc {
    type ArrayTy = [u8; Self::MAX]; //~ ERROR generic `Self` types
}

fn main() {}


