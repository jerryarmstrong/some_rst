src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0063_variadic_fun.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    fn a(_: *mut u8, ...,);
    fn b(_: *mut u8, _: ...);
    fn c(_: *mut u8, #[cfg(never)] [w, t, f]: ...,);
}


