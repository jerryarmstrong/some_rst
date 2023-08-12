tests/ui/attributes/unix_sigpipe/unix_sigpipe-duplicates.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unix_sigpipe)]

#[unix_sigpipe = "sig_ign"]
#[unix_sigpipe = "inherit"] //~ error: multiple `unix_sigpipe` attributes
fn main() {}


