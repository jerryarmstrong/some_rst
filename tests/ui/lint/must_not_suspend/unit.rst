tests/ui/lint/must_not_suspend/unit.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
#![feature(must_not_suspend)]
#![deny(must_not_suspend)]

#[must_not_suspend = "You gotta use Umm's, ya know?"]
struct Umm {
    i: i64
}


fn bar() -> Umm {
    Umm {
        i: 1
    }
}

async fn other() {}

pub async fn uhoh() {
    let _guard = bar(); //~ ERROR `Umm` held across
    other().await;
}

fn main() {
}


