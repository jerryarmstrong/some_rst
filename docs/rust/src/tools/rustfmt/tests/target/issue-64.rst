src/tools/rustfmt/tests/target/issue-64.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue 64

pub fn header_name<T: Header>() -> &'static str {
    let name = <T as Header>::header_name();
    let func = <T as Header>::header_name;
    name
}


