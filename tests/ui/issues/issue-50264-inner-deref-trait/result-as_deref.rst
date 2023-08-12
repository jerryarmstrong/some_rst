tests/ui/issues/issue-50264-inner-deref-trait/result-as_deref.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _result = &Ok(42).as_deref();
//~^ ERROR the method
}


