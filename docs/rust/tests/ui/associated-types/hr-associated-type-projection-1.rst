tests/ui/associated-types/hr-associated-type-projection-1.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait UnsafeCopy<'a, T: Copy>
where
    for<'b> <Self as UnsafeCopy<'b, T>>::Item: std::ops::Deref<Target = T>,
{
    type Item;

    fn bug(item: &Self::Item) -> () {
        let x: T = **item;
        &x as *const _;
    }
}

impl<T: Copy + std::ops::Deref> UnsafeCopy<'_, T> for T {
    //~^ type mismatch resolving `<T as Deref>::Target == T`
    type Item = T;
}

pub fn main() {
    <&'static str>::bug(&"");
}


