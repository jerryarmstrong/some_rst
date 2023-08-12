tests/ui/feature-gates/trace_macros-gate.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the trace_macros feature gate is on.

fn main() {
    trace_macros!(); //~ ERROR `trace_macros` is not stable
                     //~| ERROR trace_macros! accepts only `true` or `false`
    trace_macros!(true); //~ ERROR `trace_macros` is not stable
    trace_macros!(false); //~ ERROR `trace_macros` is not stable

    macro_rules! expando {
        ($x: ident) => { trace_macros!($x) } //~ ERROR `trace_macros` is not stable
    }

    expando!(true);
}


