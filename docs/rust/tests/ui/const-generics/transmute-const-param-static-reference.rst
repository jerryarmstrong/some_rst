tests/ui/const-generics/transmute-const-param-static-reference.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: full min
//[full] check-pass

#![cfg_attr(full, feature(adt_const_params))]
#![cfg_attr(full, allow(incomplete_features))]

struct Const<const P: &'static ()>;
//[min]~^ ERROR `&'static ()` is forbidden as the type of a const generic parameter

fn main() {
    const A: &'static () = unsafe {
        std::mem::transmute(10 as *const ())
    };

    let _ = Const::<{A}>;
}


