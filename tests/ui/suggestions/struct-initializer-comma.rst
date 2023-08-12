tests/ui/suggestions/struct-initializer-comma.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

pub struct Foo {
    pub first: bool,
    pub second: u8,
}

fn main() {
    let _ = Foo {
        //~^ ERROR missing field
        first: true
        second: 25
        //~^ ERROR expected one of
    };
}


