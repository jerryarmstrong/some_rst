tests/mir-opt/byte_slice.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z mir-opt-level=0

// EMIT_MIR byte_slice.main.SimplifyCfg-elaborate-drops.after.mir
fn main() {
    let x = b"foo";
    let y = [5u8, b'x'];
}


