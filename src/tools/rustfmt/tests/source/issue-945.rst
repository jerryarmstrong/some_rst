src/tools/rustfmt/tests/source/issue-945.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl Bar { default const unsafe fn foo() { "hi" } }

impl Baz { default unsafe extern "C" fn foo() { "hi" } }

impl Foo for Bar { default fn foo() { "hi" } }


