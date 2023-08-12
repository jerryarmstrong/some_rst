tests/run-make-fulldeps/allow-warnings-cmdline-stability/bar.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![feature(staged_api)]
#![unstable(feature = "unstable_test_feature", issue = "none")]

pub fn baz() {}


