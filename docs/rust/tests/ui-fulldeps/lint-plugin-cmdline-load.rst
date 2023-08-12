tests/ui-fulldeps/lint-plugin-cmdline-load.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:lint-plugin-test.rs
// ignore-stage1
// compile-flags: -Z crate-attr=plugin(lint_plugin_test)

#![feature(plugin)]

fn lintme() { } //~ WARNING item is named 'lintme'

#[allow(test_lint)]
pub fn main() {
    fn lintme() { }
}


