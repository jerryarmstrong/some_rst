src/tools/miri/tests/pass/main_fn.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(imported_main)]

mod foo {
    pub(crate) fn bar() {}
}

use foo::bar as main;


