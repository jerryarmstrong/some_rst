tests/ui/consts/min_const_fn/cmp_fn_pointers.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const fn cmp(x: fn(), y: fn()) -> bool {
    unsafe { x == y }
    //~^ ERROR can't compare
}

fn main() {}


