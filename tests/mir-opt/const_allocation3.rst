tests/mir-opt/const_allocation3.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: ConstProp
// ignore-endian-big
// EMIT_MIR_FOR_EACH_BIT_WIDTH
// EMIT_MIR const_allocation3.main.ConstProp.after.mir
fn main() {
    FOO;
}

#[repr(packed)]
struct Packed {
    a: [u8; 28],
    b: &'static i32,
    c: u32,
    d: [u8; 102],
    e: fn(),
    f: u16,
    g: &'static u8,
    h: [u8; 20],
}

static FOO: &Packed = &Packed {
    a: [0xAB; 28],
    b: &42,
    c: 0xABCD_EF01,
    d: [0; 102],
    e: main,
    f: 0,
    g: &[0; 100][99],
    h: [0; 20],
};


