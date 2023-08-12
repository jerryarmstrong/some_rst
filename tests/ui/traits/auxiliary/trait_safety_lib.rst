tests/ui/traits/auxiliary/trait_safety_lib.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Simple smoke test that unsafe traits can be compiled etc.

pub unsafe trait Foo {
    fn foo(&self) -> isize;
}

unsafe impl Foo for isize {
    fn foo(&self) -> isize { *self }
}


