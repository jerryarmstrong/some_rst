tests/ui/hygiene/auxiliary/def-site-async-await.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

extern crate opaque_hygiene;

pub async fn serve() {
    opaque_hygiene::make_it!();
}


