tests/ui/static/static-mut-not-constant.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_syntax)]

static mut a: Box<isize> = box 3;
//~^ ERROR allocations are not allowed in statics

fn main() {}


