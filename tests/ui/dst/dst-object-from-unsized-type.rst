tests/ui/dst/dst-object-from-unsized-type.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we cannot create objects from unsized types.

trait Foo { fn foo(&self) {} }
impl Foo for str {}
impl Foo for [u8] {}

fn test1<T: ?Sized + Foo>(t: &T) {
    let u: &dyn Foo = t;
    //~^ ERROR the size for values of type
}

fn test2<T: ?Sized + Foo>(t: &T) {
    let v: &dyn Foo = t as &dyn Foo;
    //~^ ERROR the size for values of type
}

fn test3() {
    let _: &[&dyn Foo] = &["hi"];
    //~^ ERROR the size for values of type
}

fn test4(x: &[u8]) {
    let _: &dyn Foo = x as &dyn Foo;
    //~^ ERROR the size for values of type
}

fn main() { }


