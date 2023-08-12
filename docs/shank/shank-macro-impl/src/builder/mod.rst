shank-macro-impl/src/builder/mod.rs
===================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    mod argument;
#[allow(clippy::module_inception)]
mod builder;

pub use argument::*;
pub use builder::*;

#[cfg(test)]
mod argument_test;
#[cfg(test)]
mod builder_test;


