src/tools/miri/tests/fail/shims/fs/mkstemp_immutable_arg.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows
//@compile-flags: -Zmiri-disable-isolation

fn main() {
    test_mkstemp_immutable_arg();
}

fn test_mkstemp_immutable_arg() {
    let s: *mut libc::c_char = b"fooXXXXXX\0" as *const _ as *mut _;
    let _fd = unsafe { libc::mkstemp(s) }; //~ ERROR: Undefined Behavior: writing to alloc1 which is read-only
}


