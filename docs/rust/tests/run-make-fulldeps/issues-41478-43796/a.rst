tests/run-make-fulldeps/issues-41478-43796/a.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
pub struct V<S>(#[allow(unused_tuple_struct_fields)] S);
pub trait An {
    type U;
}
pub trait F<A> {
}
impl<A: An> F<A> for V<<A as An>::U> {
}


