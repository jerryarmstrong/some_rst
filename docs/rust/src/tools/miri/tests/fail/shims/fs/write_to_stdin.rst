src/tools/miri/tests/fail/shims/fs/write_to_stdin.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows

fn main() -> std::io::Result<()> {
    let bytes = b"hello";
    unsafe {
        libc::write(0, bytes.as_ptr() as *const libc::c_void, 5); //~ ERROR: cannot write to stdin
    }
    Ok(())
}


