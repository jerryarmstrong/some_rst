tests/elfs/bss_section.rs
=========================

Last edited: 2023-08-10 08:46:13

Contents:

.. code-block:: rs

    static mut VAL: u64 = 0;

#[no_mangle]
pub fn entrypoint() -> u64 {
    unsafe { core::ptr::write_volatile(&mut VAL, 42); }
    return 0;
}


