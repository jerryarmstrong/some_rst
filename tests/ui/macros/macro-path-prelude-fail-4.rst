tests/ui/macros/macro-path-prelude-fail-4.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(inline)] //~ ERROR expected derive macro, found built-in attribute `inline`
struct S;

fn main() {}


