tests/ui/attributes/unix_sigpipe/unix_sigpipe.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unix_sigpipe)]

#[unix_sigpipe] //~ error: valid values for `#[unix_sigpipe = "..."]` are `inherit`, `sig_ign`, or `sig_dfl`
fn main() {}


