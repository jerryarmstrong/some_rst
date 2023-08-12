tests/ui/attributes/unix_sigpipe/unix_sigpipe-error.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:sigpipe-utils.rs

#![feature(unix_sigpipe)]

#[unix_sigpipe = "sig_ign"]
fn main() {
    extern crate sigpipe_utils;

    // #[unix_sigpipe = "sig_ign"] is active, so the legacy behavior of ignoring
    // SIGPIPE shall be in effect
    sigpipe_utils::assert_sigpipe_handler(sigpipe_utils::SignalHandler::Ignore);
}


