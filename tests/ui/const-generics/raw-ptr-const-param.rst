tests/ui/const-generics/raw-ptr-const-param.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: full min

#![cfg_attr(full, feature(adt_const_params))]
#![cfg_attr(full, allow(incomplete_features))]

struct Const<const P: *const u32>; //~ ERROR: using raw pointers as const generic parameters

fn main() {
    let _: Const<{ 15 as *const _ }> = Const::<{ 10 as *const _ }>;
    let _: Const<{ 10 as *const _ }> = Const::<{ 10 as *const _ }>;
}


