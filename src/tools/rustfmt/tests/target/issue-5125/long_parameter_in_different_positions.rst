src/tools/rustfmt/tests/target/issue-5125/long_parameter_in_different_positions.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn middle(
    a: usize,
    b: <u16 as intercom::type_system::ExternType<
        intercom::type_system::AutomationTypeSystem,
    >>::ForeignType,
    c: bool,
) {
}

fn last(
    a: usize,
    b: <u16 as intercom::type_system::ExternType<
        intercom::type_system::AutomationTypeSystem,
    >>::ForeignType,
) {
}

fn first(
    a: <u16 as intercom::type_system::ExternType<
        intercom::type_system::AutomationTypeSystem,
    >>::ForeignType,
    b: usize,
) {
}


