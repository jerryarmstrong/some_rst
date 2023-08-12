tests/ui/extern/extern-type-diag-not-similar.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // We previously mentioned other extern types in the error message here.
//
// Two extern types shouldn't really be considered similar just
// because they are both extern types.

#![feature(extern_types)]
extern {
    type ShouldNotBeMentioned;
}

extern {
    type Foo;
}

unsafe impl Send for ShouldNotBeMentioned {}

fn assert_send<T: Send + ?Sized>() {}

fn main() {
    assert_send::<Foo>()
    //~^ ERROR `Foo` cannot be sent between threads safely
}


