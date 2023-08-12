tests/ui/builtin-superkinds/auxiliary/trait_superkinds_in_metadata.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test library crate for cross-crate usages of traits inheriting
// from the builtin kinds. Mostly tests metadata correctness.

#![crate_type="lib"]

pub trait RequiresShare : Sync { }
pub trait RequiresRequiresShareAndSend : RequiresShare + Send { }
pub trait RequiresCopy : Copy { }


