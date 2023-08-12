tests/ui/attributes/unix_sigpipe/unix_sigpipe-crate.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unix_sigpipe)]
#![unix_sigpipe = "inherit"] //~ error: `unix_sigpipe` attribute cannot be used at crate level

fn main() {}


