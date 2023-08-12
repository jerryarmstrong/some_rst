tests/ui/parser/bounds-type.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z parse-only

struct S<
    T: 'a + Tr, // OK
    T: Tr + 'a, // OK
    T: 'a, // OK
    T:, // OK
    T: ?for<'a> Trait, // OK
    T: Tr +, // OK
    T: ?'a, //~ ERROR `?` may only modify trait bounds, not lifetime bounds

    T: ~const Tr, // OK
    T: ~const ?Tr, // OK
    T: ~const Tr + 'a, // OK
    T: ~const 'a, //~ ERROR `~const` may only modify trait bounds, not lifetime bounds
>;

fn main() {}


