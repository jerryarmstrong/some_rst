tests/elfs/rodata_section.rs
============================

Last edited: 2023-08-10 08:46:13

Contents:

.. code-block:: rs

    static _VAL_A: u64 = 41;
static VAL_B: u64 = 42;
static _VAL_C: u64 = 43;

#[no_mangle]
pub fn entrypoint() -> u64 {
    return unsafe { core::ptr::read_volatile(&VAL_B) };
}

