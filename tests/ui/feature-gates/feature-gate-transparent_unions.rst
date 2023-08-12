tests/ui/feature-gates/feature-gate-transparent_unions.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(transparent)]
union OkButUnstableUnion { //~ ERROR transparent unions are unstable
    field: u8,
    zst: (),
}

fn main() {}


