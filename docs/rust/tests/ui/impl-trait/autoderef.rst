tests/ui/impl-trait/autoderef.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

use std::path::Path;
use std::ffi::OsStr;
use std::ops::Deref;

fn frob(path: &str) -> impl Deref<Target = Path> + '_ {
    OsStr::new(path).as_ref()
}

fn open_parent<'path>(_path: &'path Path) {
    todo!()
}

fn main() {
    let old_path = frob("hello");

    open_parent(&old_path);
}


