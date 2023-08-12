tests/ui/rfc-2627-raw-dylib/unsupported-abi.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-x86_64
// only-windows
// compile-flags: --crate-type lib --emit link
#[link(name = "foo", kind = "raw-dylib")]
extern "stdcall" {
    fn f(x: i32);
    //~^ ERROR ABI not supported by `#[link(kind = "raw-dylib")]` on this architecture
}

pub fn lib_main() {
    unsafe { f(42); }
}


