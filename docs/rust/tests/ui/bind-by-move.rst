tests/ui/bind-by-move.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::sync::Arc;
fn dispose(_x: Arc<bool>) { }

pub fn main() {
    let p = Arc::new(true);
    let x = Some(p);
    match x {
        Some(z) => { dispose(z); },
        None => panic!()
    }
}


