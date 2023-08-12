src/tools/miri/tests/pass/shims/env/home.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: home_dir is not supported on Windows
//@compile-flags: -Zmiri-disable-isolation
use std::env;

fn main() {
    env::remove_var("HOME"); // make sure we enter the interesting codepath
    #[allow(deprecated)]
    env::home_dir().unwrap();
}


