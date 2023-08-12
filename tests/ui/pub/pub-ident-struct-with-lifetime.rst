tests/ui/pub/pub-ident-struct-with-lifetime.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub S<'a> {
//~^ ERROR missing `struct` for struct definition
}
fn main() {}


