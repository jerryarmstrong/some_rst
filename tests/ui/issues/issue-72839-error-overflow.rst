tests/ui/issues/issue-72839-error-overflow.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #72839
// Tests that we do not overflow during trait selection after
// a type error occurs
use std::ops::Rem;
trait Foo {}
struct MyStruct<T>(T);

impl<T, U> Rem<MyStruct<T>> for MyStruct<U> where MyStruct<U>: Rem<MyStruct<T>> {
    type Output = u8;
    fn rem(self, _: MyStruct<T>) -> Self::Output {
        panic!()
    }
}

fn main() {}

fn foo() {
    if missing_var % 8 == 0 {} //~ ERROR cannot find
}


