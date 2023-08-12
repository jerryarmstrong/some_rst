tests/ui/derives/derive-renamed.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018

use derive as my_derive;

#[my_derive(Debug)]
struct S;

fn main() {
    println!("{:?}", S); // OK
}


