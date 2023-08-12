tests/rustdoc/type-layout-flag-required.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that `--show-type-layout` is required in order to show layout info.

// @!hasraw type_layout_flag_required/struct.Foo.html 'Size: '
pub struct Foo(usize);


