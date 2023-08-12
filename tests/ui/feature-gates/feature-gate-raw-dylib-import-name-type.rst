tests/ui/feature-gates/feature-gate-raw-dylib-import-name-type.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-windows
// only-x86
#[link(name = "foo", kind = "raw-dylib", import_name_type = "decorated")]
//~^ ERROR link kind `raw-dylib` is unstable on x86
//~| ERROR import name type is unstable
extern "C" {}

fn main() {}


