tests/ui/feature-gates/feature-gate-native_link_modifiers_as_needed.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "foo", kind = "dylib", modifiers = "+as-needed")]
//~^ ERROR: linking modifier `as-needed` is unstable
extern "C" {}

fn main() {}


