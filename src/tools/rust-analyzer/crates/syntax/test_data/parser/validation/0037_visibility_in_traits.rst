src/tools/rust-analyzer/crates/syntax/test_data/parser/validation/0037_visibility_in_traits.rs
==============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl T for () {
    fn foo() {}
    pub fn bar() {}
    pub(crate) type Baz = ();
    pub(crate) const C: i32 = 92;
}


