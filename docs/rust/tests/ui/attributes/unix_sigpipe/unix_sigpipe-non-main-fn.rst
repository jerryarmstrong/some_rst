tests/ui/attributes/unix_sigpipe/unix_sigpipe-non-main-fn.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unix_sigpipe)]

#[unix_sigpipe = "inherit"] //~ error: `unix_sigpipe` attribute can only be used on `fn main()`
fn f() {}

fn main() {}


