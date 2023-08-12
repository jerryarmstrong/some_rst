tests/ui/privacy/pub-priv-dep/std-pub.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // The 'std' crates should always be implicitly public,
// without having to pass any compiler arguments

// run-pass

#![deny(exported_private_dependencies)]

pub struct PublicType {
    pub field: Option<u8>
}

fn main() {}


