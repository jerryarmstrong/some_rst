src/tools/rustfmt/tests/source/issue-2482/a.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-reorder_modules: true

// Do not reorder inline modules.

mod c;
mod a {
    fn a() {}
}
mod b;


