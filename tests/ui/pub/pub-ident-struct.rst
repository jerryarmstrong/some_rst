tests/ui/pub/pub-ident-struct.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

pub S {
//~^ ERROR missing `struct` for struct definition
}
fn main() {}


