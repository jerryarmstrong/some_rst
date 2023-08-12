tests/ui/coherence/coherence-negative-impls-safe-rpass.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

#![feature(negative_impls)]

use std::marker::Send;

struct TestType;

impl !Send for TestType {}

fn main() {}


