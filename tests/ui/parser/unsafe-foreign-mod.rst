tests/ui/parser/unsafe-foreign-mod.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    unsafe extern "C" {
    //~^ ERROR extern block cannot be declared unsafe
}

fn main() {}


