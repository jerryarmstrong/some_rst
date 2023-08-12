tests/ui/resolve/extern-prelude-fail.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--extern extern_prelude
// aux-build:extern-prelude.rs

// Extern prelude names are not available by absolute paths

fn main() {
    use extern_prelude::S; //~ ERROR unresolved import `extern_prelude`
    let s = ::extern_prelude::S; //~ ERROR failed to resolve
}


