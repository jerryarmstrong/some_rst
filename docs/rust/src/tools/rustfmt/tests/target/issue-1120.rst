src/tools/rustfmt/tests/target/issue-1120.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-reorder_imports: true

// Ensure that a use at the start of an inline module is correctly formatted.
mod foo {
    use bar;
}

// Ensure that an indented `use` gets the correct indentation.
mod foo {
    use bar;
}


