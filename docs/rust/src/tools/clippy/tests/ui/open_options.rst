src/tools/clippy/tests/ui/open_options.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fs::OpenOptions;

#[allow(unused_must_use)]
#[warn(clippy::nonsensical_open_options)]
fn main() {
    OpenOptions::new().read(true).truncate(true).open("foo.txt");
    OpenOptions::new().append(true).truncate(true).open("foo.txt");

    OpenOptions::new().read(true).read(false).open("foo.txt");
    OpenOptions::new().create(true).create(false).open("foo.txt");
    OpenOptions::new().write(true).write(false).open("foo.txt");
    OpenOptions::new().append(true).append(false).open("foo.txt");
    OpenOptions::new().truncate(true).truncate(false).open("foo.txt");
}


