library/std/src/sys/solid/thread_local_key.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub type Key = usize;

#[inline]
pub unsafe fn create(_dtor: Option<unsafe extern "C" fn(*mut u8)>) -> Key {
    panic!("should not be used on the solid target");
}

#[inline]
pub unsafe fn set(_key: Key, _value: *mut u8) {
    panic!("should not be used on the solid target");
}

#[inline]
pub unsafe fn get(_key: Key) -> *mut u8 {
    panic!("should not be used on the solid target");
}

#[inline]
pub unsafe fn destroy(_key: Key) {
    panic!("should not be used on the solid target");
}


