tests/ui/suggestions/missing-lifetime-in-assoc-const-type.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait ZstAssert: Sized {
    const A: &str = ""; //~ ERROR missing lifetime specifier
    const B: S = S { s: &() }; //~ ERROR missing lifetime specifier
    const C: &'_ str = ""; //~ ERROR missing lifetime specifier
    const D: T = T { a: &(), b: &() }; //~ ERROR missing lifetime specifier
}

struct S<'a> {
    s: &'a (),
}
struct T<'a, 'b> {
    a: &'a (),
    b: &'b (),
}

fn main() {}


