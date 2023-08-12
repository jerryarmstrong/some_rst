tests/ui/const-generics/defaults/forward-declared.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<const N: usize = M, const M: usize = 10>;
//~^ ERROR generic parameters with a default cannot use forward declared identifiers

enum Bar<const N: usize = M, const M: usize = 10> {}
//~^ ERROR generic parameters with a default cannot use forward declared identifiers

struct Foo2<const N: usize = N>;
//~^ ERROR generic parameters with a default cannot use forward declared identifiers

enum Bar2<const N: usize = N> {}
//~^ ERROR generic parameters with a default cannot use forward declared identifiers

fn main() {}


