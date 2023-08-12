tests/ui/lint/unreachable-async-fn.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018

#[allow(dead_code)]
async fn foo () { // unreachable lint doesn't trigger
   unimplemented!()
}

fn main() {}


