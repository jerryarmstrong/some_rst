tests/ui/extern/extern-crate-visibility.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    extern crate core;
}

// Check that private crates can be used from outside their modules, albeit with warnings
use foo::core::cell; //~ ERROR crate import `core` is private

fn f() {
    foo::core::cell::Cell::new(0); //~ ERROR crate import `core` is private

    use foo::*;
    mod core {} // Check that private crates are not glob imported
}

mod bar {
    pub extern crate core;
}

mod baz {
    pub use bar::*;
    use self::core::cell; // Check that public extern crates are glob imported
}

fn main() {}


