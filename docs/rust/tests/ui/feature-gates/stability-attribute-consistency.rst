tests/ui/feature-gates/stability-attribute-consistency.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![stable(feature = "stable_test_feature", since = "1.0.0")]

#![feature(staged_api)]

#[stable(feature = "foo", since = "1.0.0")]
fn foo_stable_1_0_0() {}

#[stable(feature = "foo", since = "1.29.0")]
//~^ ERROR feature `foo` is declared stable since 1.29.0
fn foo_stable_1_29_0() {}

#[unstable(feature = "foo", issue = "none")]
//~^ ERROR feature `foo` is declared unstable
fn foo_unstable() {}

fn main() {}


