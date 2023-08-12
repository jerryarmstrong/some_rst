tests/ui/regions/regions-escape-via-trait-or-not.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

trait Deref {
    fn get(self) -> isize;
}

impl<'a> Deref for &'a isize {
    fn get(self) -> isize {
        *self
    }
}

fn with<R:Deref, F>(f: F) -> isize where F: FnOnce(&isize) -> R {
    f(&3).get()
}

fn return_it() -> isize {
    with(|o| o) //~ ERROR lifetime may not live long enough
}

fn main() {
}


