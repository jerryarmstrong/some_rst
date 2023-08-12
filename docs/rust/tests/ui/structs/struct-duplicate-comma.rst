tests/ui/structs/struct-duplicate-comma.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// Issue #50974

pub struct Foo {
    pub a: u8,
    pub b: u8
}

fn main() {
    let _ = Foo {
        a: 0,,
          //~^ ERROR expected identifier
        b: 42
    };
}


