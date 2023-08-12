tests/ui/rfc-2091-track-caller/error-with-invalid-abi.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[track_caller]
extern "C" fn f() {}
//~^^ ERROR `#[track_caller]` requires Rust ABI

extern "C" {
    #[track_caller]
    fn g();
    //~^^ ERROR `#[track_caller]` requires Rust ABI
}

fn main() {}


