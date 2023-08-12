tests/ui/feature-gates/feature-gate-log_syntax.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    log_syntax!() //~ ERROR `log_syntax!` is not stable enough
}


