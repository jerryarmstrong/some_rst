tests/ui/feature-gates/feature-gate-default_type_parameter_fallback.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused)]

fn avg<T=i32>(_: T) {}
//~^ ERROR defaults for type parameters are only allowed
//~| WARN this was previously accepted

struct S<T>(T);
impl<T=i32> S<T> {}
//~^ ERROR defaults for type parameters are only allowed
//~| WARN this was previously accepted

fn main() {}


