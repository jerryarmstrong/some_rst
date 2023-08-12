tests/run-make-fulldeps/extern-fn-with-union/testcrate.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

#[repr(C)]
pub struct TestUnion {
    _val: u64,
}

#[link(name = "ctest", kind = "static")]
extern "C" {
    pub fn give_back(tu: TestUnion) -> u64;
}


