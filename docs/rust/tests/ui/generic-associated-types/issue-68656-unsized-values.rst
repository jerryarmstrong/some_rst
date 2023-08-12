tests/ui/generic-associated-types/issue-68656-unsized-values.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #68656

trait UnsafeCopy<T: Copy> {
    type Item<'a>: std::ops::Deref<Target = T>;

    fn bug<'a>(item: &Self::Item<'a>) -> () {
        let x: T = **item;
        &x as *const _;
    }
}

impl<T: Copy + std::ops::Deref> UnsafeCopy<T> for T {
    type Item<'a> = T;
    //~^ ERROR type mismatch resolving `<T as Deref>::Target == T`
}

fn main() {
    <&'static str>::bug(&"");
}


