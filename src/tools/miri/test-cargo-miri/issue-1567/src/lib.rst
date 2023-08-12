src/tools/miri/test-cargo-miri/issue-1567/src/lib.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use byteorder::{BigEndian, ByteOrder};

pub fn use_the_dependency() {
    let _n = <BigEndian as ByteOrder>::read_u32(&[1, 2, 3, 4]);
}


