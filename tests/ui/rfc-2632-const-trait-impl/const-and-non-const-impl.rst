tests/ui/rfc-2632-const-trait-impl/const-and-non-const-impl.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

pub struct Int(i32);

impl const std::ops::Add for i32 {
    //~^ ERROR only traits defined in the current crate can be implemented for primitive types
    type Output = Self;

    fn add(self, rhs: Self) -> Self {
        self + rhs
    }
}

impl std::ops::Add for Int {
    type Output = Self;

    fn add(self, rhs: Self) -> Self {
        Int(self.0 + rhs.0)
    }
}

impl const std::ops::Add for Int {
    //~^ ERROR conflicting implementations of trait
    type Output = Self;

    fn add(self, rhs: Self) -> Self {
        Int(self.0 + rhs.0)
    }
}

fn main() {}


