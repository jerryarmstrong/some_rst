tests/ui/rfc-2008-non-exhaustive/auxiliary/variants.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

pub enum NonExhaustiveVariants {
    #[non_exhaustive] Unit,
    #[non_exhaustive] Tuple(u32),
    #[non_exhaustive] Struct { field: u32 }
}


