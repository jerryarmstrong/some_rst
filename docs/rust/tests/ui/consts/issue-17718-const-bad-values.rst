tests/ui/consts/issue-17718-const-bad-values.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const C1: &'static mut [usize] = &mut [];
//~^ ERROR: mutable references are not allowed

static mut S: usize = 3;
const C2: &'static mut usize = unsafe { &mut S };
//~^ ERROR: constants cannot refer to statics
//~| ERROR: constants cannot refer to statics

fn main() {}


