tests/ui/consts/min_const_fn/min_const_unsafe_fn_libstd_stability.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![unstable(feature = "humans",
            reason = "who ever let humans program computers,
            we're apparently really bad at it",
            issue = "none")]

#![feature(const_fn_floating_point_arithmetic, foo, foo2)]
#![feature(staged_api)]

#[stable(feature = "rust1", since = "1.0.0")]
#[rustc_const_unstable(feature="foo", issue = "none")]
const unsafe fn foo() -> u32 { 42 }

#[stable(feature = "rust1", since = "1.0.0")]
#[rustc_const_stable(feature = "rust1", since = "1.0.0")]
// can't call non-min_const_fn
const unsafe fn bar() -> u32 { unsafe { foo() } } //~ ERROR not yet stable as a const fn

#[unstable(feature = "foo2", issue = "none")]
const unsafe fn foo2() -> u32 { 42 }

#[stable(feature = "rust1", since = "1.0.0")]
#[rustc_const_stable(feature = "rust1", since = "1.0.0")]
// can't call non-min_const_fn
const unsafe fn bar2() -> u32 { unsafe { foo2() } } //~ ERROR not yet stable as a const fn

#[stable(feature = "rust1", since = "1.0.0")]
#[rustc_const_stable(feature = "rust1", since = "1.0.0")]
// conformity is required
const unsafe fn bar3() -> u32 { (5f32 + 6f32) as u32 }
//~^ ERROR const-stable function cannot use `#[feature(const_fn_floating_point_arithmetic)]`

// check whether this function cannot be called even with the feature gate active
#[unstable(feature = "foo2", issue = "none")]
const unsafe fn foo2_gated() -> u32 { 42 }

#[stable(feature = "rust1", since = "1.0.0")]
#[rustc_const_stable(feature = "rust1", since = "1.0.0")]
// can't call non-min_const_fn
const unsafe fn bar2_gated() -> u32 { unsafe { foo2_gated() } }
//~^ ERROR not yet stable as a const fn

fn main() {}


