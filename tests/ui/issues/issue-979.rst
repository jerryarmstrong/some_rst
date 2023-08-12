tests/ui/issues/issue-979.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

use std::cell::Cell;

struct r<'a> {
    b: &'a Cell<isize>,
}

impl<'a> Drop for r<'a> {
    fn drop(&mut self) {
        self.b.set(self.b.get() + 1);
    }
}

fn r(b: &Cell<isize>) -> r {
    r {
        b: b
    }
}

pub fn main() {
    let b = &Cell::new(0);
    {
        let _p = Some(r(b));
    }

    assert_eq!(b.get(), 1);
}


