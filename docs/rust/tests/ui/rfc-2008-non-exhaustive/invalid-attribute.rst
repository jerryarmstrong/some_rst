tests/ui/rfc-2008-non-exhaustive/invalid-attribute.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[non_exhaustive(anything)]
//~^ ERROR malformed `non_exhaustive` attribute
struct Foo;

#[non_exhaustive]
//~^ ERROR attribute should be applied to a struct or enum [E0701]
trait Bar { }

#[non_exhaustive]
//~^ ERROR attribute should be applied to a struct or enum [E0701]
union Baz {
    f1: u16,
    f2: u16
}

fn main() { }


