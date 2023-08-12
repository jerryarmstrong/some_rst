tests/ui/derives/derive-multiple-with-packed.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#[derive(Clone, Copy)]
#[derive(Debug)] // OK, even if `Copy` is in the different `#[derive]`
#[repr(packed)]
struct CacheRecordHeader {
    field: u64,
}

fn main() {}


