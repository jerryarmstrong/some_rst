tests/ui-fulldeps/plugin-args.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:empty-plugin.rs
// ignore-stage1

#![feature(plugin)]
#![plugin(empty_plugin(args))]
//~^ ERROR malformed `plugin` attribute
//~| WARNING compiler plugins are deprecated

fn main() {}


