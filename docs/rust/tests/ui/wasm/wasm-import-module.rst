tests/ui/wasm/wasm-import-module.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(link_cfg)]

#[link(name = "...", wasm_import_module)] //~ ERROR: must be of the form
extern "C" {}

#[link(name = "...", wasm_import_module(x))] //~ ERROR: must be of the form
extern "C" {}

#[link(name = "...", wasm_import_module())] //~ ERROR: must be of the form
extern "C" {}

#[link(wasm_import_module = "foo", name = "bar")] //~ ERROR: `wasm_import_module` is incompatible with other arguments
extern "C" {}

#[link(wasm_import_module = "foo", kind = "dylib")] //~ ERROR: `wasm_import_module` is incompatible with other arguments
extern "C" {}

#[link(wasm_import_module = "foo", cfg(FALSE))] //~ ERROR: `wasm_import_module` is incompatible with other arguments
extern "C" {}

fn main() {}


