tests/ui/errors/auxiliary/remapped_dep.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --remap-path-prefix={{src-base}}/errors/auxiliary=remapped-aux
// no-remap-src-base: Manually remap, so the remapped path remains in .stderr file.

pub struct SomeStruct {} // This line should be show as part of the error.


