tests/ui/internal/internal-unstable-thread-local.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:internal_unstable.rs

#![allow(dead_code)]

extern crate internal_unstable;


thread_local!(static FOO: () = ());
thread_local!(static BAR: () = internal_unstable::unstable()); //~ ERROR use of unstable

fn main() {}


