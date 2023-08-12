tests/ui/nll/constant.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that MIR borrowck and NLL analysis can handle constants of
// arbitrary types without ICEs.

// check-pass

const HI: &str = "hi";

fn main() {
    assert_eq!(HI, "hi");
}


