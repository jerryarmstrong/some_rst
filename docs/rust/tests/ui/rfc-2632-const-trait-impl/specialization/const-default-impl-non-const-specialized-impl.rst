tests/ui/rfc-2632-const-trait-impl/specialization/const-default-impl-non-const-specialized-impl.rs
==================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that specializing trait impls must be at least as const as the default impl.

#![feature(const_trait_impl)]
#![feature(min_specialization)]

#[const_trait]
trait Value {
    fn value() -> u32;
}

impl<T> const Value for T {
    default fn value() -> u32 {
        0
    }
}

struct FortyTwo;

impl Value for FortyTwo { //~ ERROR cannot specialize on const impl with non-const impl
    fn value() -> u32 {
        println!("You can't do that (constly)");
        42
    }
}

fn main() {}


