tests/run-make-fulldeps/compiler-lookup-paths/d.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#[link(name = "native", kind = "static")]
extern "C" {}


