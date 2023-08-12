tests/ui/consts/write_to_static_via_mut_ref.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_mut_refs)]

static OH_NO: &mut i32 = &mut 42; //~ ERROR mutable references are not allowed
fn main() {
    assert_eq!(*OH_NO, 42);
    *OH_NO = 43; //~ ERROR cannot assign to `*OH_NO`, as `OH_NO` is an immutable static
}


