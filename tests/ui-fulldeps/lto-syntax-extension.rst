tests/ui-fulldeps/lto-syntax-extension.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:lto-syntax-extension-lib.rs
// aux-build:lto-syntax-extension-plugin.rs
// compile-flags:-C lto
// ignore-stage1
// no-prefer-dynamic

#![feature(plugin)]
#![plugin(lto_syntax_extension_plugin)] //~ WARNING compiler plugins are deprecated

extern crate lto_syntax_extension_lib;

fn main() {
    lto_syntax_extension_lib::foo();
}


