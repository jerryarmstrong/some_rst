tests/ui/issues/issue-4735.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use std::mem::transmute;

struct NonCopyable(*const u8);

impl Drop for NonCopyable {
    fn drop(&mut self) {
        let NonCopyable(p) = *self;
        let _v = unsafe { transmute::<*const u8, Box<isize>>(p) };
    }
}

pub fn main() {
    let t = Box::new(0);
    let p = unsafe { transmute::<Box<isize>, *const u8>(t) };
    let _z = NonCopyable(p);
}


