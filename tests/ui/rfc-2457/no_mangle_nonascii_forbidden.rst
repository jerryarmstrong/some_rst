tests/ui/rfc-2457/no_mangle_nonascii_forbidden.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
pub fn řųśť() {}  //~ `#[no_mangle]` requires ASCII identifier

pub struct Foo;

impl Foo {
    #[no_mangle]
    pub fn řųśť() {}  //~ `#[no_mangle]` requires ASCII identifier
}

trait Bar {
    fn řųśť();
}

impl Bar for Foo {
    #[no_mangle]
    fn řųśť() {}  //~ `#[no_mangle]` requires ASCII identifier
}

fn main() {}


