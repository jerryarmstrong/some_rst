tests/ui/imports/issue-2937.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use m::f as x; //~ ERROR unresolved import `m::f` [E0432]
               //~^ no `f` in `m`

mod m {}

fn main() {}


