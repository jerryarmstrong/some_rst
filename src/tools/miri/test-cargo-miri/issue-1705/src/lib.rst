src/tools/miri/test-cargo-miri/issue-1705/src/lib.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use byteorder::{ByteOrder, LittleEndian};

pub fn use_the_dependency() {
    let _n = <LittleEndian as ByteOrder>::read_u32(&[1, 2, 3, 4]);
}


