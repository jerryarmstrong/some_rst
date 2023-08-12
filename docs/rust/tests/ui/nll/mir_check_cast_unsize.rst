tests/ui/nll/mir_check_cast_unsize.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

use std::fmt::Debug;

fn bar<'a>(x: &'a u32) -> &'static dyn Debug {
    x
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


