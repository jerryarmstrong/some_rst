tests/ui/rfc-2008-non-exhaustive/auxiliary/monovariants.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[non_exhaustive]
pub enum NonExhaustiveMonovariant {
    Variant(u32),
}

pub enum ExhaustiveMonovariant {
    Variant(u32),
}


