tests/ui/nll/user-annotations/inherent-associated-constants.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A<'a>(&'a ());

impl A<'static> {
    const IC: i32 = 10;
}

fn non_wf_associated_const<'a>(x: i32) {
    A::<'a>::IC; //~ ERROR lifetime may not live long enough
}

fn wf_associated_const<'a>(x: i32) {
    A::<'static>::IC;
}

fn main() {}


