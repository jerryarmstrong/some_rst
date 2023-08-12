tests/ui/feature-gates/feature-gate-cfg_sanitize.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(not(sanitize = "thread"))]
//~^ `cfg(sanitize)` is experimental
fn main() {}


