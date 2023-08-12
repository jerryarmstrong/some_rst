tests/ui/attributes/unix_sigpipe/unix_sigpipe-list.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unix_sigpipe)]

#[unix_sigpipe(inherit)] //~ error: malformed `unix_sigpipe` attribute input
fn main() {}


