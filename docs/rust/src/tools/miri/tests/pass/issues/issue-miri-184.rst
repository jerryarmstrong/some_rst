src/tools/miri/tests/pass/issues/issue-miri-184.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    let bytes: [u8; 8] = unsafe { ::std::mem::transmute(0u64) };
    let _val: &[u8] = &bytes;
}


