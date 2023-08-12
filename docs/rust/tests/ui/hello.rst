tests/ui/hello.rs
=================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// revisions: e2015 e2018 e2021 e2024

//[e2018] edition:2018
//[e2021] edition:2021
//[e2024] edition:2024

//[e2024] compile-flags: -Zunstable-options

fn main() {
    println!("hello");
}


