tests/ui-fulldeps/lint-group-plugin-deny-cmdline.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:lint-group-plugin-test.rs
// ignore-stage1
// compile-flags: -D lint-me

#![feature(plugin)]

#![plugin(lint_group_plugin_test)]
//~^ WARN use of deprecated attribute `plugin`

fn lintme() { } //~ ERROR item is named 'lintme'

fn pleaselintme() { } //~ ERROR item is named 'pleaselintme'

pub fn main() {
    lintme();
    pleaselintme();
}


