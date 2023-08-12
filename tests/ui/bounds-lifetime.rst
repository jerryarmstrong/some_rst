tests/ui/bounds-lifetime.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A = for<'b, 'a: 'b> fn(); //~ ERROR lifetime bounds cannot be used in this context
type B = for<'b, 'a: 'b,> fn(); //~ ERROR lifetime bounds cannot be used in this context
type C = for<'b, 'a: 'b +> fn(); //~ ERROR lifetime bounds cannot be used in this context
type D = for<'a, T> fn(); //~ ERROR only lifetime parameters can be used in this context
type E = dyn for<T> Fn(); //~ ERROR only lifetime parameters can be used in this context

fn main() {}


