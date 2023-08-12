tests/ui/rfc-2627-raw-dylib/link-ordinal-multiple.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-windows
#![cfg_attr(target_arch = "x86", feature(raw_dylib))]

#[link(name = "foo", kind = "raw-dylib")]
extern "C" {
    #[link_ordinal(1)] //~ ERROR multiple `link_ordinal` attributes
    #[link_ordinal(2)]
    fn foo();
    #[link_ordinal(1)] //~ ERROR multiple `link_ordinal` attributes
    #[link_ordinal(2)]
    static mut imported_variable: i32;
}

fn main() {}


