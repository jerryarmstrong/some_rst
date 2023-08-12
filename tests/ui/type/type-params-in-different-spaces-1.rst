tests/ui/type/type-params-in-different-spaces-1.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::Add;

trait BrokenAdd: Copy + Add<Output=Self> {
    fn broken_add<T>(&self, rhs: T) -> Self {
        *self + rhs //~  ERROR mismatched types
                    //~| expected type parameter `Self`, found type parameter `T`
                    //~| expected type parameter `Self`
                    //~| found type parameter `T`
    }
}

impl<T: Copy + Add<Output=T>> BrokenAdd for T {}

pub fn main() {
    let foo: u8 = 0;
    let x: u8 = foo.broken_add("hello darkness my old friend".to_string());
    println!("{}", x);
}


