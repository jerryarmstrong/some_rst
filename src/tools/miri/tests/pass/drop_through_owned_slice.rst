src/tools/miri/tests/pass/drop_through_owned_slice.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Bar;

static mut DROP_COUNT: usize = 0;

impl Drop for Bar {
    fn drop(&mut self) {
        unsafe {
            DROP_COUNT += 1;
        }
    }
}

fn main() {
    let b: Box<[Bar]> = vec![Bar, Bar, Bar, Bar].into_boxed_slice();
    assert_eq!(unsafe { DROP_COUNT }, 0);
    drop(b);
    assert_eq!(unsafe { DROP_COUNT }, 4);
}


