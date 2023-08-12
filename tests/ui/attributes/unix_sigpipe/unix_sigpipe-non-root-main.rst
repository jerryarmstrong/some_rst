tests/ui/attributes/unix_sigpipe/unix_sigpipe-non-root-main.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unix_sigpipe)]

mod m {
    #[unix_sigpipe = "inherit"] //~ error: `unix_sigpipe` attribute can only be used on root `fn main()`
    fn main() {}
}

fn main() {}


