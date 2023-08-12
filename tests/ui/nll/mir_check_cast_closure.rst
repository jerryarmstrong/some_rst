tests/ui/nll/mir_check_cast_closure.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

fn bar<'a, 'b>() -> fn(&'a u32, &'b u32) -> &'a u32 {
    let g: fn(_, _) -> _ = |_x, y| y;
    g
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


