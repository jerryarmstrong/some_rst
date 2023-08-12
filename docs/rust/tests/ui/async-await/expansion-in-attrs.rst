tests/ui/async-await/expansion-in-attrs.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018

macro_rules! with_doc {
    ($doc: expr) => {
        #[doc = $doc]
        async fn f() {}
    };
}

with_doc!(concat!(""));

fn main() {}


