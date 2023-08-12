tests/ui-fulldeps/multiple-plugins.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:multiple-plugins-1.rs
// aux-build:multiple-plugins-2.rs
// ignore-stage1

// Check that the plugin registrar of multiple plugins doesn't conflict

#![feature(plugin)]
#![plugin(multiple_plugins_1)] //~ WARN use of deprecated attribute `plugin`
#![plugin(multiple_plugins_2)] //~ WARN use of deprecated attribute `plugin`

fn main() {}


