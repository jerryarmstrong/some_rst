tests/ui/stdlib-unit-tests/eq-multidispatch.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(PartialEq, Debug)]
struct Bar;
#[derive(Debug)]
struct Baz;
#[derive(Debug)]
struct Foo;
#[derive(Debug)]
struct Fu;

impl PartialEq for Baz { fn eq(&self, _: &Baz) -> bool  { true } }

impl PartialEq<Fu> for Foo { fn eq(&self, _: &Fu) -> bool { true } }
impl PartialEq<Foo> for Fu { fn eq(&self, _: &Foo) -> bool { true } }

impl PartialEq<Bar> for Foo { fn eq(&self, _: &Bar) -> bool { false } }
impl PartialEq<Foo> for Bar { fn eq(&self, _: &Foo) -> bool { false } }

fn main() {
    assert!(Bar != Foo);
    assert!(Foo != Bar);

    assert_eq!(Bar, Bar);

    assert_eq!(Baz, Baz);

    assert_eq!(Foo, Fu);
    assert_eq!(Fu, Foo);
}


