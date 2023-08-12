tests/ui/rfc-2632-const-trait-impl/nested-closure.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(const_trait_impl, once_cell)]

use std::sync::LazyLock;

static EXTERN_FLAGS: LazyLock<String> = LazyLock::new(|| {
    let x = || String::new();
    x()
});

fn main() {}


