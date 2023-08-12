tests/elfs/reloc_64_64.rs
=========================

Last edited: 2023-08-10 08:46:13

Contents:

.. code-block:: rs

    #[no_mangle]
pub fn entrypoint() -> u64 {
    return entrypoint as u64;
}


