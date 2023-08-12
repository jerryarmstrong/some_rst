src/tools/miri/tests/fail/validity/invalid_wide_raw.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(invalid_value)]

fn main() {
    trait T {}
    #[derive(Debug)]
    struct S {
        #[allow(dead_code)]
        x: *mut dyn T,
    }
    dbg!(S { x: unsafe { std::mem::transmute((0usize, 0usize)) } }); //~ ERROR: encountered null pointer, but expected a vtable pointer
}


