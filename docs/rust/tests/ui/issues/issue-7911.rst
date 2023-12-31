tests/ui/issues/issue-7911.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// (Closes #7911) Test that we can use the same self expression
// with different mutability in macro in two methods

#![allow(unused_variables)] // unused foobar_immut + foobar_mut
trait FooBar {
    fn dummy(&self) { }
}
struct Bar(#[allow(unused_tuple_struct_fields)] i32);
struct Foo { bar: Bar }

impl FooBar for Bar {}

trait Test {
    fn get_immut(&self) -> &dyn FooBar;
    fn get_mut(&mut self) -> &mut dyn FooBar;
}

macro_rules! generate_test { ($type_:path, $slf:ident, $field:expr) => (
    impl Test for $type_ {
        fn get_immut(&$slf) -> &dyn FooBar {
            &$field as &dyn FooBar
        }

        fn get_mut(&mut $slf) -> &mut dyn FooBar {
            &mut $field as &mut dyn FooBar
        }
    }
)}

generate_test!(Foo, self, self.bar);

pub fn main() {
    let mut foo: Foo = Foo { bar: Bar(42) };
    { let foobar_immut = foo.get_immut(); }
    { let foobar_mut = foo.get_mut(); }
}


