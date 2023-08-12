tests/codegen/no-plt.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C relocation-model=pic -Z plt=no

#![crate_type = "lib"]

// We need a function which is normally called through the PLT.
extern "C" {
    // CHECK: Function Attrs:{{.*}}nonlazybind
    fn getenv(name: *const u8) -> *mut u8;
}

// Ensure the function gets referenced.
pub unsafe fn call_through_plt() -> *mut u8 {
    getenv(b"\0".as_ptr())
}

// Ensure intrinsics also skip the PLT
// CHECK: !"RtLibUseGOT"


