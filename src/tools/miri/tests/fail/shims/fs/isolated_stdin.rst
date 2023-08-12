src/tools/miri/tests/fail/shims/fs/isolated_stdin.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows

fn main() -> std::io::Result<()> {
    let mut bytes = [0u8; 512];
    unsafe {
        libc::read(0, bytes.as_mut_ptr() as *mut libc::c_void, 512); //~ ERROR: `read` from stdin not available when isolation is enabled
    }
    Ok(())
}


