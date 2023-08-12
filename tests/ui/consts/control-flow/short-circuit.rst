tests/ui/consts/control-flow/short-circuit.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Test that both `&&` and `||` actually short-circuit.
// Formerly, both sides were evaluated unconditionally

const TRUE: bool = true || panic!();
const FALSE: bool = false && panic!();

fn main() {
    assert!(TRUE);
    assert!(!FALSE);
}


