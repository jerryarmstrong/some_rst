tests/ui/linkage-attr/auxiliary/link-cfg-works-transitive-rlib.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

#![feature(link_cfg)]
#![crate_type = "rlib"]

#[link(name = "foo", cfg(foo))]
extern "C" {}


