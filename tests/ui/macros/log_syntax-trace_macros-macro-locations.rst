tests/ui/macros/log_syntax-trace_macros-macro-locations.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#![feature(trace_macros, log_syntax)]

// make sure these macros can be used as in the various places that
// macros can occur.

// items
trace_macros!(false);
log_syntax!();

fn main() {

    // statements
    trace_macros!(false);
    log_syntax!();

    // expressions
    (trace_macros!(false),
     log_syntax!());
}


