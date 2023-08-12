tests/ui/abi/abi-typo-unstable.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rust-intrinsic is unstable and not enabled, so it should not be suggested as a fix
extern "rust-intrinsec" fn rust_intrinsic() {} //~ ERROR invalid ABI

fn main() {
    rust_intrinsic();
}


