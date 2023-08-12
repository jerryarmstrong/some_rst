tests/ui/nll/issue-21114-ebfull.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

use std::collections::HashMap;
use std::sync::Mutex;

fn i_used_to_be_able_to(foo: &Mutex<HashMap<usize, usize>>) -> Vec<(usize, usize)> {
    let mut foo = foo.lock().unwrap();

    foo.drain().collect()
}

fn but_after_nightly_update_now_i_gotta(foo: &Mutex<HashMap<usize, usize>>) -> Vec<(usize, usize)> {
    let mut foo = foo.lock().unwrap();

    return foo.drain().collect();
}

fn main() {}


