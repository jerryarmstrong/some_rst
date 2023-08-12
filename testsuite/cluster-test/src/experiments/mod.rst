testsuite/cluster-test/src/experiments/mod.rs
=============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    mod reboot_random_validator;

pub use reboot_random_validator::RebootRandomValidators;
use std::{collections::HashSet, fmt::Display};

pub trait Experiment: Display + Send {
    fn affected_validators(&self) -> HashSet<String>;
    fn run(&self) -> failure::Result<()>;
}


