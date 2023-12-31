tests/rustdoc/decl-trailing-whitespace.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for <https://github.com/rust-lang/rust/issues/98803>.

#![crate_name = "foo"]

pub struct Error;

// @has 'foo/trait.Write.html'

pub trait Write {
    // @snapshot 'declaration' - '//*[@class="item-decl"]//code'
    fn poll_write(
        self: Option<String>,
        cx: &mut Option<String>,
        buf: &mut [usize]
    ) -> Option<Result<usize, Error>>;
    fn poll_flush(
        self: Option<String>,
        cx: &mut Option<String>
    ) -> Option<Result<(), Error>>;
    fn poll_close(
        self: Option<String>,
        cx: &mut Option<String>,
    ) -> Option<Result<(), Error>>;

    fn poll_write_vectored(
        self: Option<String>,
        cx: &mut Option<String>,
        bufs: &[usize]
    ) -> Option<Result<usize, Error>> {}
}


