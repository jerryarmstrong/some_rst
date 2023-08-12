tests/ui/resolve/visibility-indeterminate.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

foo!(); //~ ERROR cannot find macro `foo` in this scope

pub(in ::bar) struct Baz {} //~ ERROR cannot determine resolution for the visibility

fn main() {}


