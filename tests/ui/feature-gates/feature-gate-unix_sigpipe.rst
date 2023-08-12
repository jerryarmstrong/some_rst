tests/ui/feature-gates/feature-gate-unix_sigpipe.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "bin"]

#[unix_sigpipe = "inherit"] //~ the `#[unix_sigpipe]` attribute is an experimental feature
fn main () {}


