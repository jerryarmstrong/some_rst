tests/ui/wf/wf-impl-associated-type-region.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we require that associated types in an impl are well-formed.



pub trait Foo<'a> {
    type Bar;
}

impl<'a, T> Foo<'a> for T {
    type Bar = &'a T; //~ ERROR E0309
}


fn main() { }


