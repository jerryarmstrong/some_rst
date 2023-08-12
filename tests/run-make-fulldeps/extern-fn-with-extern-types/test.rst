tests/run-make-fulldeps/extern-fn-with-extern-types/test.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]

#[link(name = "ctest", kind = "static")]
extern "C" {
    type data;

    fn data_create(magic: u32) -> *mut data;
    fn data_get(data: *mut data) -> u32;
}

const MAGIC: u32 = 0xdeadbeef;
fn main() {
    unsafe {
        let data = data_create(MAGIC);
        assert_eq!(data_get(data), MAGIC);
    }
}


