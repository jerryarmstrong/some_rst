tests/ui/consts/min_const_fn/bad_const_fn_body_ice.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const fn foo(a: i32) -> Vec<i32> {
    vec![1, 2, 3]
    //~^ ERROR allocations are not allowed
    //~| ERROR cannot call non-const fn
}

fn main() {}


