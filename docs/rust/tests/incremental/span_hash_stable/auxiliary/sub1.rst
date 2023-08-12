tests/incremental/span_hash_stable/auxiliary/sub1.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[rustc_clean(cfg="rpass2")]
pub struct SomeType {
    pub x: u32,
    pub y: i64,
}


