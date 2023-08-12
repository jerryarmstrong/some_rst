tests/run-make-fulldeps/crate-data-smoke/crate.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// Querying about the crate metadata should *not* parse the entire crate, it
// only needs the crate attributes (which are guaranteed to be at the top) be
// sure that if we have an error like a missing module that we can still query
// about the crate id.
mod error;


