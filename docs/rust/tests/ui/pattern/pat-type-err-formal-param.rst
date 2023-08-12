tests/ui/pattern/pat-type-err-formal-param.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test the `.span_label(..)` to the type when there's a
// type error in a pattern due to a the formal parameter.

fn main() {}

struct Tuple(u8);

fn foo(Tuple(_): String) {} //~ ERROR mismatched types


