src/tools/miri/tests/pass/ptr_raw.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn basic_raw() {
    let mut x = 12;
    let x = &mut x;

    assert_eq!(*x, 12);

    let raw = x as *mut i32;
    unsafe {
        *raw = 42;
    }

    assert_eq!(*x, 42);

    let raw = x as *mut i32;
    unsafe {
        *raw = 12;
    }
    *x = 23;

    assert_eq!(*x, 23);
}

fn main() {
    basic_raw();
}


