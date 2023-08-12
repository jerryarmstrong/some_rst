tests/ui/rust-2018/uniform-paths/prelude-fail-2.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// Built-in attribute
use inline as imported_inline;
mod builtin {
    pub use inline as imported_inline;
}

// Tool module
use rustfmt as imported_rustfmt;
mod tool_mod {
    pub use rustfmt as imported_rustfmt;
}

#[imported_inline] //~ ERROR cannot use a built-in attribute through an import
#[builtin::imported_inline] //~ ERROR cannot use a built-in attribute through an import
#[imported_rustfmt::skip] //~ ERROR cannot use a tool module through an import
                          //~| ERROR cannot use a tool module through an import
#[tool_mod::imported_rustfmt::skip] //~ ERROR cannot use a tool module through an import
                                    //~| ERROR cannot use a tool module through an import
fn main() {}


