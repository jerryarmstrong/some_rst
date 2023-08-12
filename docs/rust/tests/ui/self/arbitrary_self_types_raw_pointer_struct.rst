tests/ui/self/arbitrary_self_types_raw_pointer_struct.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(arbitrary_self_types)]

use std::rc::Rc;

struct Foo(String);

impl Foo {
    unsafe fn foo(self: *const Self) -> *const str {
        (*self).0.as_ref()
    }

    fn complicated_1(self: *const Rc<Self>) -> &'static str {
        "Foo::complicated_1"
    }

    unsafe fn complicated_2(self: Rc<*const Self>) -> *const str {
        (**self).0.as_ref()
    }
}

fn main() {
    let foo = Foo("abc123".into());
    assert_eq!("abc123", unsafe { &*(&foo as *const Foo).foo() });
    assert_eq!("Foo::complicated_1", std::ptr::null::<Rc<Foo>>().complicated_1());
    let rc = Rc::new(&foo as *const Foo);
    assert_eq!("abc123", unsafe { &*rc.complicated_2()});
}


