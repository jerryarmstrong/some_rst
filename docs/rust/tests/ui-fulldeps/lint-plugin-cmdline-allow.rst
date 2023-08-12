tests/ui-fulldeps/lint-plugin-cmdline-allow.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:lint-plugin-test.rs
// ignore-stage1
// compile-flags: -A test-lint

#![feature(plugin)]
#![plugin(lint_plugin_test)] //~ WARNING compiler plugins are deprecated

fn lintme() { }

pub fn main() {
}


