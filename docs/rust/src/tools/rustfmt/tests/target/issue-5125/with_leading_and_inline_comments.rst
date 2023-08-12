src/tools/rustfmt/tests/target/issue-5125/with_leading_and_inline_comments.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(
    // Pre Comment
    a: <u16 as intercom::type_system::ExternType<
        intercom::type_system::AutomationTypeSystem,
    >>::ForeignType, // Inline comment
) {
}


