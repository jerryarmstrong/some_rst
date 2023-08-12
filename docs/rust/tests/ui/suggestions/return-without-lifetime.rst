tests/ui/suggestions/return-without-lifetime.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Thing<'a>(&'a ());
struct Foo<'a>(&usize);
//~^ ERROR missing lifetime specifier

fn func1<'a>(_arg: &'a Thing) -> &() { unimplemented!() }
//~^ ERROR missing lifetime specifier
fn func2<'a>(_arg: &Thing<'a>) -> &() { unimplemented!() }
//~^ ERROR missing lifetime specifier

fn main() {}


