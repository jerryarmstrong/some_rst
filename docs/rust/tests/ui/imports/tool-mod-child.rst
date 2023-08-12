tests/ui/imports/tool-mod-child.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use clippy::a; //~ ERROR unresolved import `clippy`
use clippy::a::b; //~ ERROR failed to resolve: maybe a missing crate `clippy`?

use rustdoc::a; //~ ERROR unresolved import `rustdoc`
use rustdoc::a::b; //~ ERROR failed to resolve: maybe a missing crate `rustdoc`?

fn main() {}


