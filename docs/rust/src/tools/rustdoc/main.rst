src/tools/rustdoc/main.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unix_sigpipe)]

#[unix_sigpipe = "sig_dfl"]
fn main() {
    rustdoc::main()
}


