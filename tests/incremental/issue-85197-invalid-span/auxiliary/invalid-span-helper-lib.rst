tests/incremental/issue-85197-invalid-span/auxiliary/invalid-span-helper-lib.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: rpass1 rpass2

extern crate respan;

#[macro_use]
#[path = "invalid-span-helper-mod.rs"]
mod invalid_span_helper_mod;

// Invoke a macro from a different file - this
// allows us to get tokens with spans from different files
helper!(1);


