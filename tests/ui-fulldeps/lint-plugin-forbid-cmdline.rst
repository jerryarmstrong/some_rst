tests/ui-fulldeps/lint-plugin-forbid-cmdline.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:lint-plugin-test.rs
// ignore-stage1
// compile-flags: -F test-lint

#![feature(plugin)]
#![plugin(lint_plugin_test)]
//~^ WARN use of deprecated attribute `plugin`
fn lintme() { } //~ ERROR item is named 'lintme'

#[allow(test_lint)] //~ ERROR allow(test_lint) incompatible
                    //~| ERROR allow(test_lint) incompatible

pub fn main() {
    lintme();
}


