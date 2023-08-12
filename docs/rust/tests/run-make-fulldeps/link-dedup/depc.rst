tests/run-make-fulldeps/link-dedup/depc.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#[link(name = "testa")]
extern "C" {}


