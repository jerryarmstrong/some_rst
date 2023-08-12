pool/examples/simple/src/lib.rs
===============================

Last edited: 2021-05-20 03:21:28

Contents:

.. code-block:: rs

    use serum_pool::{declare_pool_entrypoint, Pool};

enum SimplePool {}

impl Pool for SimplePool {}

#[cfg(not(feature = "no-entrypoint"))]
declare_pool_entrypoint!(SimplePool);


