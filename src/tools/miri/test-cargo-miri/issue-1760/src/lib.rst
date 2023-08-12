src/tools/miri/test-cargo-miri/issue-1760/src/lib.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use proc_macro::TokenStream;

#[cfg(miri)]
compile_error!("`miri` cfg should not be set in proc-macro");

#[proc_macro]
pub fn use_the_dependency(_: TokenStream) -> TokenStream {
    TokenStream::new()
}


