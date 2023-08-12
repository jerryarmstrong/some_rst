tests/elfs/syscall_static.rs
============================

Last edited: 2023-08-10 08:46:13

Contents:

.. code-block:: rs

    mod syscalls;

#[no_mangle]
pub fn entrypoint() -> u64 {
    unsafe { syscalls::log(b"foo\n".as_ptr(), 4); }
    return 0;
}


