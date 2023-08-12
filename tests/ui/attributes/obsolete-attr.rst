tests/ui/attributes/obsolete-attr.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Obsolete attributes fall back to unstable custom attributes.

#[ab_isize = "stdcall"] extern "C" {}
//~^ ERROR cannot find attribute `ab_isize` in this scope

#[fixed_stack_segment] fn f() {}
//~^ ERROR cannot find attribute `fixed_stack_segment` in this scope

fn main() {}


