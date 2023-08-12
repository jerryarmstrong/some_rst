tests/ui/proc-macro/derive-multiple-with-packed.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#[derive(Clone, Copy)]
#[derive(Debug)] // OK, even if `Copy` is in the different `#[derive]`
#[derive(PartialEq)] // OK too
#[repr(packed)]
struct CacheRecordHeader {
    field: u64,
}

fn main() {}


