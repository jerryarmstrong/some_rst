tests/ui/nll/promoted-liveness.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that promoted that have larger mir bodies than their containing function
// don't cause an ICE.

// check-pass

fn main() {
    &["0", "1", "2", "3", "4", "5", "6", "7"];
}


