tests/ui/issues/auxiliary/issue-5518.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A<'a, T> {
    fn f(&mut self) -> &'a mut T;
    fn p() -> T;
}


