src/tools/miri/tests/pass/zst_variant_drop.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;
impl Drop for Foo {
    fn drop(&mut self) {
        unsafe {
            FOO = true;
        }
    }
}

static mut FOO: bool = false;

enum Bar {
    A(Box<i32>),
    B(Foo),
}

fn main() {
    assert!(unsafe { !FOO });
    drop(Bar::A(Box::new(42)));
    assert!(unsafe { !FOO });
    drop(Bar::B(Foo));
    assert!(unsafe { FOO });
}


