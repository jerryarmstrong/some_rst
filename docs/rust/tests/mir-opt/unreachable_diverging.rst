tests/mir-opt/unreachable_diverging.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum Empty {}

fn empty() -> Option<Empty> {
    None
}

fn loop_forever() {
    loop {}
}

// EMIT_MIR unreachable_diverging.main.UnreachablePropagation.diff
fn main() {
    let x = true;
    if let Some(bomb) = empty() {
        if x {
            loop_forever()
        }
        match bomb {}
    }
}


