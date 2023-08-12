tests/ui/entry-point/imported_main_unused_not_trigger_feature_gate.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(rustc_attrs)]

#[rustc_main]
fn actual_main() {}

mod foo {
    pub(crate) fn something() {}
}

use foo::something as main;


