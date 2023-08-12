tests/ui/resolve/name-collision-in-trait-fn-sig.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// This is currently stable behavior, which was almost accidentally made an
// error in #102161 since there is no test exercising it. I am not sure if
// this _should_ be the desired behavior, but at least we should know if it
// changes.

fn main() {}

trait Foo {
    fn fn_with_type_named_same_as_local_in_param(b: i32, b: i32);
}


