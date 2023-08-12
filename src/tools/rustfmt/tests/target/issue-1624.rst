src/tools/rustfmt/tests/target/issue-1624.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #1624
pub unsafe fn some_long_function_name(
    arg1: Type1,
    arg2: Type2,
) -> (SomeLongTypeName, AnotherLongTypeName, AnotherLongTypeName) {
}


