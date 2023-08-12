tests/ui/proc-macro/not-joint.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:not-joint.rs

extern crate not_joint as bar;
use bar::{tokens, nothing};

tokens![< -];

#[nothing]
a![< -];

#[nothing]
b!{< -}

#[nothing]
c!(< -);

#[nothing]
fn foo() {
    //! dox
    let x = 2 < - 3;
}

fn main() {}


