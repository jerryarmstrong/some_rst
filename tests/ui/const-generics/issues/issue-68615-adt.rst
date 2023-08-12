tests/ui/const-generics/issues/issue-68615-adt.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // [full] check-pass
// revisions: full min
#![cfg_attr(full, feature(adt_const_params))]
#![cfg_attr(full, allow(incomplete_features))]

struct Const<const V: [usize; 0]> {}
//[min]~^ ERROR `[usize; 0]` is forbidden as the type of a const generic parameter
type MyConst = Const<{ [] }>;

fn main() {
    let _x = Const::<{ [] }> {};
    let _y = MyConst {};
}


