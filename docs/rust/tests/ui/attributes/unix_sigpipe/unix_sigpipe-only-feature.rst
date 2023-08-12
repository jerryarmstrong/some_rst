tests/ui/attributes/unix_sigpipe/unix_sigpipe-only-feature.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:sigpipe-utils.rs

#![feature(unix_sigpipe)]

fn main() {
    extern crate sigpipe_utils;

    // Only #![feature(unix_sigpipe)] is enabled, not #[unix_sigpipe = "..."].
    // This shall not change any behavior, so we still expect SIGPIPE to be
    // ignored
    sigpipe_utils::assert_sigpipe_handler(sigpipe_utils::SignalHandler::Ignore);
}


