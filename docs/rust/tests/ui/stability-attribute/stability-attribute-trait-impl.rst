tests/ui/stability-attribute/stability-attribute-trait-impl.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api, never_type, c_unwind)]
//~^ ERROR module has missing stability attribute

#[stable(feature = "a", since = "1")]
struct StableType;

#[unstable(feature = "b", issue = "none")]
struct UnstableType;

#[stable(feature = "c", since = "1")]
trait StableTrait {}

#[unstable(feature = "d", issue = "none")]
trait UnstableTrait {}

#[unstable(feature = "e", issue = "none")]
impl UnstableTrait for UnstableType {}

#[unstable(feature = "f", issue = "none")]
impl StableTrait for UnstableType {}

#[unstable(feature = "g", issue = "none")]
impl UnstableTrait for StableType {}

#[unstable(feature = "h", issue = "none")]
impl StableTrait for ! {}

// Note: If C-unwind is stabilized, switch this to another (unstable) ABI.
#[unstable(feature = "i", issue = "none")]
impl StableTrait for extern "C-unwind" fn() {}

#[unstable(feature = "j", issue = "none")]
//~^ ERROR an `#[unstable]` annotation here has no effect [ineffective_unstable_trait_impl]
impl StableTrait for StableType {}

#[unstable(feature = "k", issue = "none")]
//~^ ERROR an `#[unstable]` annotation here has no effect [ineffective_unstable_trait_impl]
impl StableTrait for fn() -> ! {}

#[unstable(feature = "l", issue = "none")]
impl StableTrait for fn() -> UnstableType {}

fn main() {}


