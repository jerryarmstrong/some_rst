tests/ui/rfc-2627-raw-dylib/link-ordinal-missing-argument.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![cfg_attr(target_arch = "x86", feature(raw_dylib))]

#[link(name = "foo")]
extern "C" {
    #[link_ordinal()]
    //~^ ERROR incorrect number of arguments to `#[link_ordinal]`
    fn foo();
    #[link_ordinal()]
    //~^ ERROR incorrect number of arguments to `#[link_ordinal]`
    static mut imported_variable: i32;
}

fn main() {}


