tests/ui/packed/issue-27060-rpass.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#[repr(packed)]
pub struct Good {
    data: &'static u32,
    data2: [&'static u32; 2],
    aligned: [u8; 32],
}

// kill this test when that turns to a hard error
#[allow(unaligned_references)]
fn main() {
    let good = Good { data: &0, data2: [&0, &0], aligned: [0; 32] };

    let _ = &good.data; // ok
    let _ = &good.data2[0]; // ok

    let _ = &good.data;
    let _ = &good.data2[0];
    let _ = &*good.data; // ok, behind a pointer
    let _ = &good.aligned; // ok, has align 1
    let _ = &good.aligned[2]; // ok, has align 1
}


