tests/ui-fulldeps/lint-plugin-deny-attr.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:lint-plugin-test.rs
// ignore-stage1

#![feature(plugin)]
#![plugin(lint_plugin_test)]
//~^ WARN use of deprecated attribute `plugin`
#![deny(test_lint)]

fn lintme() { } //~ ERROR item is named 'lintme'

pub fn main() {
    lintme();
}


