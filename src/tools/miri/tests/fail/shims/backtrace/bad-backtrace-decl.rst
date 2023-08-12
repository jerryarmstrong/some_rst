src/tools/miri/tests/fail/shims/backtrace/bad-backtrace-decl.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "Rust" {
    fn miri_get_backtrace(flags: u64) -> Box<[*mut ()]>;
    fn miri_resolve_frame(ptr: *mut (), flags: u64);
}

fn main() {
    let frames = unsafe { miri_get_backtrace(0) };
    for frame in frames.into_iter() {
        unsafe {
            miri_resolve_frame(*frame, 0); //~ ERROR: Undefined Behavior: bad declaration of miri_resolve_frame - should return a struct with 5 fields
        }
    }
}


