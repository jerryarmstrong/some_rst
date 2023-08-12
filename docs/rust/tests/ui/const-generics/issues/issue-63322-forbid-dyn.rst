tests/ui/const-generics/issues/issue-63322-forbid-dyn.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: full min
#![cfg_attr(full, feature(adt_const_params))]
#![cfg_attr(full, allow(incomplete_features))]

trait A {}
struct B;
impl A for B {}

fn test<const T: &'static dyn A>() {
    //[full]~^ ERROR must be annotated with `#[derive(PartialEq, Eq)]` to be used
    //[min]~^^ ERROR `&'static (dyn A + 'static)` is forbidden
    unimplemented!()
}

fn main() {
    test::<{ &B }>();
}


