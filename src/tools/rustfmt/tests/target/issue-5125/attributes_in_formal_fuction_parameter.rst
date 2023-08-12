src/tools/rustfmt/tests/target/issue-5125/attributes_in_formal_fuction_parameter.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(
    #[unused] a: <u16 as intercom::type_system::ExternType<
        intercom::type_system::AutomationTypeSystem,
    >>::ForeignType,
) {
}


