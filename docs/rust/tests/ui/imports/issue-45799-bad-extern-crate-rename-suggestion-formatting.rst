tests/ui/imports/issue-45799-bad-extern-crate-rename-suggestion-formatting.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

extern crate std;
fn main() {}
//~^^ ERROR the name `std` is defined multiple times [E0259]


