tests/ui/macros/trace_macros-format.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trace_macros)]

fn main() {
    trace_macros!(); //~ ERROR trace_macros! accepts only `true` or `false`
    trace_macros!(1); //~ ERROR trace_macros! accepts only `true` or `false`
    trace_macros!(ident); //~ ERROR trace_macros! accepts only `true` or `false`
    trace_macros!(for); //~ ERROR trace_macros! accepts only `true` or `false`
    trace_macros!(true,); //~ ERROR trace_macros! accepts only `true` or `false`
    trace_macros!(false 1); //~ ERROR trace_macros! accepts only `true` or `false`


    // should be fine:
    macro_rules! expando {
        ($x: ident) => { trace_macros!($x) }
    }

    expando!(true);
}


