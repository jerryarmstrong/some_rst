src/tools/rustfmt/tests/target/issue-3585/extern_crate.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-inline_attribute_width: 100

#[macro_use] extern crate static_assertions;

#[cfg(unix)] extern crate static_assertions;

// a comment before the attribute
#[macro_use]
// some comment after
extern crate static_assertions;


