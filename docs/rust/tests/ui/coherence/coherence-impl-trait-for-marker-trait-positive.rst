tests/ui/coherence/coherence-impl-trait-for-marker-trait-positive.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]
#![feature(negative_impls)]

// Test for issue #56934 - that it is impossible to redundantly
// implement an auto-trait for a trait object type that contains it.

// Positive impl variant.

auto trait Marker1 {}
auto trait Marker2 {}

trait Object: Marker1 {}

// A supertrait marker is illegal...
impl Marker1 for dyn Object + Marker2 { }   //~ ERROR E0371
// ...and also a direct component.
impl Marker2 for dyn Object + Marker2 { }   //~ ERROR E0371

// But implementing a marker if it is not present is OK.
impl Marker2 for dyn Object {} // OK

// A non-principal trait-object type is orphan even in its crate.
unsafe impl Send for dyn Marker2 {} //~ ERROR E0117

// And impl'ing a remote marker for a local trait object is forbidden
// by one of these special orphan-like rules.
unsafe impl Send for dyn Object {} //~ ERROR E0321
unsafe impl Send for dyn Object + Marker2 {} //~ ERROR E0321

fn main() { }


