tests/mir-opt/nrvo_simple.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: RenameReturnPlace

// EMIT_MIR nrvo_simple.nrvo.RenameReturnPlace.diff
fn nrvo(init: fn(&mut [u8; 1024])) -> [u8; 1024] {
    let mut buf = [0; 1024];
    init(&mut buf);
    buf
}

fn main() {
    let _ = nrvo(|buf| { buf[4] = 4; });
}


