tests/ui/attributes/unix_sigpipe/unix_sigpipe-sig_dfl.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:sigpipe-utils.rs

#![feature(unix_sigpipe)]

#[unix_sigpipe = "sig_dfl"]
fn main() {
    extern crate sigpipe_utils;

    // #[unix_sigpipe = "sig_dfl"] is active, so SIGPIPE shall NOT be ignored, instead
    // the default handler shall be installed
    sigpipe_utils::assert_sigpipe_handler(sigpipe_utils::SignalHandler::Default);
}


