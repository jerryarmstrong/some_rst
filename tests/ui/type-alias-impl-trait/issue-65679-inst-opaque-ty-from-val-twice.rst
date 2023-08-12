tests/ui/type-alias-impl-trait/issue-65679-inst-opaque-ty-from-val-twice.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zsave-analysis
// check-pass

#![feature(type_alias_impl_trait, rustc_attrs)]

type T = impl Sized;
// The concrete type referred by impl-trait-type-alias(`T`) is guaranteed
// to be the same as where it occurs, whereas `impl Trait`'s instance is location sensitive;
// so difference assertion should not be declared on impl-trait-type-alias's instances.
// for details, check RFC-2515:
// https://github.com/rust-lang/rfcs/blob/master/text/2515-type_alias_impl_trait.md

fn take(_: fn() -> T) {}

fn main() {
    take(|| {});
    take(|| {});
}


