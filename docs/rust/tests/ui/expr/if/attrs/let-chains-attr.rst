tests/ui/expr/if/attrs/let-chains-attr.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(let_chains)]

#[cfg(FALSE)]
fn foo() {
    #[attr]
    if let Some(_) = Some(true) && let Ok(_) = Ok(1) {
    } else if let Some(false) = Some(true) {
    }
}

fn main() {}


