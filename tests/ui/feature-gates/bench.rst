tests/ui/feature-gates/bench.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#[bench] //~ ERROR use of unstable library feature 'test'
         //~| WARN this was previously accepted
fn bench() {}

use bench as _; //~ ERROR use of unstable library feature 'test'
                //~| WARN this was previously accepted
fn main() {}


