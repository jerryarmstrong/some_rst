tests/ui-fulldeps/lint-group-plugin.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:lint-group-plugin-test.rs
// ignore-stage1

#![feature(plugin)]
#![plugin(lint_group_plugin_test)] //~ WARNING use of deprecated attribute
#![allow(dead_code)]

fn lintme() { } //~ WARNING item is named 'lintme'
fn pleaselintme() { } //~ WARNING item is named 'pleaselintme'

#[allow(lint_me)]
pub fn main() {
    fn lintme() { }

    fn pleaselintme() { }
}


