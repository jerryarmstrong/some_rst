tests/ui/associated-item/associated-item-enum.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Enum { Variant }

impl Enum {
    const MISSPELLABLE: i32 = 0;
    fn misspellable() {}
}

trait Trait {
    fn misspellable_trait() {}
}

impl Trait for Enum {
    fn misspellable_trait() {}
}

fn main() {
    Enum::mispellable(); //~ ERROR no variant or associated item
    Enum::mispellable_trait(); //~ ERROR no variant or associated item
    Enum::MISPELLABLE; //~ ERROR no variant or associated item
}


