src/tools/clippy/tests/ui/filetype_is_file.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::filetype_is_file)]

fn main() -> std::io::Result<()> {
    use std::fs;
    use std::ops::BitOr;

    // !filetype.is_dir()
    if fs::metadata("foo.txt")?.file_type().is_file() {
        // read file
    }

    // positive of filetype.is_dir()
    if !fs::metadata("foo.txt")?.file_type().is_file() {
        // handle dir
    }

    // false positive of filetype.is_dir()
    if !fs::metadata("foo.txt")?.file_type().is_file().bitor(true) {
        // ...
    }

    Ok(())
}


