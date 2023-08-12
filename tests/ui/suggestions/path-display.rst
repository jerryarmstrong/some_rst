tests/ui/suggestions/path-display.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::path::{Path, PathBuf};

fn main() {
    let path = Path::new("/tmp/foo/bar.txt");
    println!("{}", path);
    //~^ ERROR E0277

    let path = PathBuf::from("/tmp/foo/bar.txt");
    println!("{}", path);
    //~^ ERROR E0277
}


