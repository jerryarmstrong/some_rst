tests/ui/attributes/unix_sigpipe/unix_sigpipe-not-used.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:sigpipe-utils.rs

fn main() {
    extern crate sigpipe_utils;

    // SIGPIPE shall be ignored since #[unix_sigpipe = "..."] is not used
    sigpipe_utils::assert_sigpipe_handler(sigpipe_utils::SignalHandler::Ignore);
}


