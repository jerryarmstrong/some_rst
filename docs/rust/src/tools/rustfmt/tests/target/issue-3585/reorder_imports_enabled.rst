src/tools/rustfmt/tests/target/issue-3585/reorder_imports_enabled.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-inline_attribute_width: 100
// rustfmt-reorder_imports: true

#[cfg(unix)] extern crate cratea;
#[cfg(unix)] extern crate crateb;

#[cfg(unix)] use cratea;
#[cfg(unix)] use crateb;


