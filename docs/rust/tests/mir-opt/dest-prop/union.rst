tests/mir-opt/dest-prop/union.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Tests that we can propagate into places that are projections into unions
// compile-flags: -Zunsound-mir-opts
fn val() -> u32 {
    1
}

// EMIT_MIR union.main.DestinationPropagation.diff
fn main() {
    union Un {
        us: u32,
    }

    let un = Un { us: val() };

    drop(unsafe { un.us });
}


