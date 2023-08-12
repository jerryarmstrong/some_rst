tests/ui/issues/issue-50264-inner-deref-trait/option-as_deref_mut.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _result = &mut Some(42).as_deref_mut();
//~^ ERROR the method
}


