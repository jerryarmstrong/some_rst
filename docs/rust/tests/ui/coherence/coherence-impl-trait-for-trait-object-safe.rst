tests/ui/coherence/coherence-impl-trait-for-trait-object-safe.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we give suitable error messages when the user attempts to
// impl a trait `Trait` for its own object type.

// If the trait is not object-safe, we give a more tailored message
// because we're such schnuckels:
trait NotObjectSafe { fn eq(&self, other: Self); }
impl NotObjectSafe for dyn NotObjectSafe { }
//~^ ERROR E0038

fn main() { }


