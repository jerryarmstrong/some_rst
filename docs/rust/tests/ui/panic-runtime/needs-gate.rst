tests/ui/panic-runtime/needs-gate.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-needs_panic_runtime
// gate-test-panic_runtime

#![panic_runtime] //~ ERROR: is an experimental feature
#![needs_panic_runtime] //~ ERROR: is an experimental feature

fn main() {}


