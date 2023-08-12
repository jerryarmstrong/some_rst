tests/ui/lint/must_not_suspend/gated.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// edition:2018
#![deny(must_not_suspend)]
//~^ WARNING unknown lint: `must_not_suspend`
//~| WARNING unknown lint: `must_not_suspend`
//~| WARNING unknown lint: `must_not_suspend`

async fn other() {}

pub async fn uhoh(m: std::sync::Mutex<()>) {
    let _guard = m.lock().unwrap();
    other().await;
}

fn main() {
}


