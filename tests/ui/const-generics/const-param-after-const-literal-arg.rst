tests/ui/const-generics/const-param-after-const-literal-arg.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct Foo<const A: usize, const B: usize>;

impl<const A: usize> Foo<1, A> {} // ok

fn main() {}


