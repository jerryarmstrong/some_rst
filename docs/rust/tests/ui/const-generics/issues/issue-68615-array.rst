tests/ui/const-generics/issues/issue-68615-array.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // [full] check-pass
// revisions: full min
#![cfg_attr(full, feature(adt_const_params))]
#![cfg_attr(full, allow(incomplete_features))]

struct Foo<const V: [usize; 0] > {}
//[min]~^ ERROR `[usize; 0]` is forbidden as the type of a const generic parameter

type MyFoo = Foo<{ [] }>;

fn main() {
    let _ = Foo::<{ [] }> {};
}


