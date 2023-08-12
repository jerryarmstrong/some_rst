tests/ui-fulldeps/feature-gate-plugin.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:empty-plugin.rs
// ignore-stage1

#![plugin(empty_plugin)]
//~^ ERROR compiler plugins are deprecated
//~| WARN use of deprecated attribute `plugin`: compiler plugins are deprecated

fn main() {}


