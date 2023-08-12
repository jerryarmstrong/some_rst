tests/ui/traits/negative-impls/rely-on-negative-impl-in-coherence.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(negative_impls)]
#![feature(with_negative_coherence)]

// aux-build: foreign_trait.rs

// Test that we cannot implement `LocalTrait` for `String`,
// even though there is a `String: !ForeignTrait` impl.
//
// This may not be the behavior we want long term, but it's the
// current semantics that we implemented so as to land `!Foo` impls
// quickly. See internals thread:
//
// https://internals.rust-lang.org/t/foo/11587/

extern crate foreign_trait;
use foreign_trait::ForeignTrait;

trait LocalTrait {}
impl<T: ForeignTrait> LocalTrait for T {}
impl LocalTrait for String {}

fn main() {}


