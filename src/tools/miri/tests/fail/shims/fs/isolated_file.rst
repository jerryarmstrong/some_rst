src/tools/miri/tests/fail/shims/fs/isolated_file.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: File handling is not implemented yet
//@error-pattern: `open` not available when isolation is enabled

fn main() {
    let _file = std::fs::File::open("file.txt").unwrap();
}


