tests/ui/resolve/crate-in-paths.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

mod bar {
    pub(crate) struct Foo;
}

fn main() {
    Foo;
    //~^ ERROR cannot find value `Foo` in this scope [E0425]
}


