src/tools/rustfmt/tests/target/mulit-file.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that where a single file is referred to in multiple places, we don't
// crash.

#[cfg(all(foo))]
#[path = "closure.rs"]
pub mod imp;

#[cfg(all(bar))]
#[path = "closure.rs"]
pub mod imp;


