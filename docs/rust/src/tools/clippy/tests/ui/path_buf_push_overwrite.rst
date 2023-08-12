src/tools/clippy/tests/ui/path_buf_push_overwrite.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
use std::path::PathBuf;

#[warn(clippy::all, clippy::path_buf_push_overwrite)]
fn main() {
    let mut x = PathBuf::from("/foo");
    x.push("/bar");
}


