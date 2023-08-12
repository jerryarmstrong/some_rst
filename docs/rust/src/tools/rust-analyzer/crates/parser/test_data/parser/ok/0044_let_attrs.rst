src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0044_let_attrs.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust-analyzer/issues/677
fn main() {
    #[cfg(feature = "backtrace")]
    let exit_code = panic::catch_unwind(move || main());
}


