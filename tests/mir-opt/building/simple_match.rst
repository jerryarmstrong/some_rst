tests/mir-opt/building/simple_match.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we don't generate unnecessarily large MIR for very simple matches


// EMIT_MIR simple_match.match_bool.built.after.mir
fn match_bool(x: bool) -> usize {
    match x {
        true => 10,
        _ => 20,
    }
}

fn main() {}


