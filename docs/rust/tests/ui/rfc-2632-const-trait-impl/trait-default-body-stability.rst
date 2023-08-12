tests/ui/rfc-2632-const-trait-impl/trait-default-body-stability.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(staged_api)]
#![feature(const_trait_impl)]
#![feature(const_t_try)]
#![feature(const_try)]
#![feature(try_trait_v2)]

#![stable(feature = "foo", since = "1.0")]

use std::ops::{ControlFlow, FromResidual, Try};

#[stable(feature = "foo", since = "1.0")]
pub struct T;

#[stable(feature = "foo", since = "1.0")]
#[rustc_const_unstable(feature = "const_t_try", issue = "none")]
impl const Try for T {
    type Output = T;
    type Residual = T;

    fn from_output(t: T) -> T {
        t
    }

    fn branch(self) -> ControlFlow<T, T> {
        ControlFlow::Continue(self)
    }
}

#[stable(feature = "foo", since = "1.0")]
#[rustc_const_unstable(feature = "const_t_try", issue = "none")]
impl const FromResidual for T {
    fn from_residual(t: T) -> T {
        t
    }
}

#[stable(feature = "foo", since = "1.0")]
#[const_trait]
pub trait Tr {
    #[stable(feature = "foo", since = "1.0")]
    fn bar() -> T {
        T?
        // Should be allowed.
        // Must enable unstable features to call this trait fn in const contexts.
    }
}

fn main() {}


