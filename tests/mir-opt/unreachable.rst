tests/mir-opt/unreachable.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Empty {}

fn empty() -> Option<Empty> {
    None
}

// EMIT_MIR unreachable.main.UnreachablePropagation.diff
fn main() {
    if let Some(_x) = empty() {
        let mut _y;

        if true {
            _y = 21;
        } else {
            _y = 42;
        }

        match _x { }
    }
}


