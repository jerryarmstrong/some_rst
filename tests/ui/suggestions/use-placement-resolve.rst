tests/ui/suggestions/use-placement-resolve.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --test
// run-rustfix
// Checks that the `use` suggestion appears *below* this inner attribute.
// There was an issue where the test synthetic #[allow(dead)] attribute on
// main which has a dummy span caused the suggestion to be placed at the top
// of the file.
#![allow(unused)]

fn main() {}

fn foobar<T: Debug>(x: T) {} //~ ERROR expected trait, found derive macro


