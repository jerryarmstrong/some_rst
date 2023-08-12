src/tools/miri/tests/pass/drop_on_fat_ptr_array_elements.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {}

struct Bar;

impl Foo for Bar {}

static mut DROP_COUNT: usize = 0;

impl Drop for Bar {
    fn drop(&mut self) {
        unsafe {
            DROP_COUNT += 1;
        }
    }
}

fn main() {
    let b: [Box<dyn Foo>; 4] = [Box::new(Bar), Box::new(Bar), Box::new(Bar), Box::new(Bar)];
    assert_eq!(unsafe { DROP_COUNT }, 0);
    drop(b);
    assert_eq!(unsafe { DROP_COUNT }, 4);
}


