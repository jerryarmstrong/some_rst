tests/ui/rfc-2627-raw-dylib/link-ordinal-too-large.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![cfg_attr(target_arch = "x86", feature(raw_dylib))]

#[link(name = "foo")]
extern "C" {
    #[link_ordinal(72436)]
    //~^ ERROR ordinal value in `link_ordinal` is too large: `72436`
    fn foo();
    #[link_ordinal(72436)]
    //~^ ERROR ordinal value in `link_ordinal` is too large: `72436`
    static mut imported_variable: i32;
}

fn main() {}


