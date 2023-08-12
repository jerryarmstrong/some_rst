tests/ui/nll/maybe-initialized-drop-uninitialized.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![allow(warnings)]

struct Wrap<'p> { p: &'p mut i32 }

impl<'p> Drop for Wrap<'p> {
    fn drop(&mut self) {
        *self.p += 1;
    }
}

fn main() {
    let mut x = 0;
    let wrap = Wrap { p: &mut x };
    std::mem::drop(wrap);
    x = 1; // OK, drop is inert
}


