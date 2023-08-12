tests/testsuite/init/empty_dir/mod.rs
=====================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use cargo_test_support::compare::assert_ui;
use cargo_test_support::prelude::*;
use cargo_test_support::{command_is_available, paths, Project};
use std::fs;
use std::process::Command;

use crate::test_root;


