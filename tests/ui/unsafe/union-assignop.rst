tests/ui/unsafe/union-assignop.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

use std::ops::AddAssign;
use std::mem::ManuallyDrop;

struct NonCopy;
impl AddAssign for NonCopy {
    fn add_assign(&mut self, _: Self) {}
}

union Foo {
    a: u8, // non-dropping
    b: ManuallyDrop<NonCopy>,
}

fn main() {
    let mut foo = Foo { a: 42 };
    foo.a += 5; //~ ERROR access to union field is unsafe
    *foo.b += NonCopy; //~ ERROR access to union field is unsafe
    *foo.b = NonCopy; //~ ERROR access to union field is unsafe
    foo.b = ManuallyDrop::new(NonCopy);
    foo.a; //~ ERROR access to union field is unsafe
    let foo = Foo { a: 42 };
    foo.b; //~ ERROR access to union field is unsafe
    let mut foo = Foo { a: 42 };
    foo.b = foo.b;
    //~^ ERROR access to union field is unsafe
}


