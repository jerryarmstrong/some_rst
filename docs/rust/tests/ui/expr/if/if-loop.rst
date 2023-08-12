tests/ui/expr/if/if-loop.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// This used to ICE because the "if" being unreachable was not handled correctly
fn err() {
    if loop {} {}
}

fn main() {}


