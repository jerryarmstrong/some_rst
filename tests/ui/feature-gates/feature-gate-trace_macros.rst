tests/ui/feature-gates/feature-gate-trace_macros.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    trace_macros!(true); //~ ERROR: `trace_macros` is not stable
}


