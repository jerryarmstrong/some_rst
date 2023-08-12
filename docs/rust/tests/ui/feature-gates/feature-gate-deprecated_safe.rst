tests/ui/feature-gates/feature-gate-deprecated_safe.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[deprecated_safe(since = "TBD", note = "...")] //~ ERROR: the `#[deprecated_safe]` attribute is an experimental feature
unsafe fn deprecated_safe_fn() {}

#[deprecated_safe(since = "TBD", note = "...")] //~ ERROR: the `#[deprecated_safe]` attribute is an experimental feature
unsafe trait DeprecatedSafeTrait {}

fn main() {}


