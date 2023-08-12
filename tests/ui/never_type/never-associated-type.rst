tests/ui/never_type/never-associated-type.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we can use ! as an associated type.

// check-pass

#![feature(never_type)]

trait Foo {
    type Wow;

    fn smeg(&self) -> Self::Wow;
}

struct Blah;
impl Foo for Blah {
    type Wow = !;
    fn smeg(&self) -> ! {
        panic!("kapow!");
    }
}

fn main() {
    Blah.smeg();
}


