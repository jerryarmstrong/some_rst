tests/ui/traits/alias/auxiliary/send_sync.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_alias)]

pub trait SendSync = Send + Sync;


