tests/ui/entry-point/imported_main_const_forbidden.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(imported_main)]
pub mod foo {
    pub const BAR: usize = 42;
}

use foo::BAR as main; //~ ERROR `main` function not found in crate


