src/tools/miri/tests/pass/drop_through_trait_object.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {}

struct Bar;

static mut DROP_CALLED: bool = false;

impl Drop for Bar {
    fn drop(&mut self) {
        unsafe {
            DROP_CALLED = true;
        }
    }
}

impl Foo for Bar {}

fn main() {
    let b: Box<dyn Foo> = Box::new(Bar);
    assert!(unsafe { !DROP_CALLED });
    drop(b);
    assert!(unsafe { DROP_CALLED });
}


