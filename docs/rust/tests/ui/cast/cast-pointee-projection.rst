tests/ui/cast/cast-pointee-projection.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Tag<'a> {
    type Type: ?Sized;
}

trait IntoRaw: for<'a> Tag<'a> {
    fn into_raw(this: *const <Self as Tag<'_>>::Type) -> *mut <Self as Tag<'_>>::Type;
}

impl<T: for<'a> Tag<'a>> IntoRaw for T {
    fn into_raw(this: *const <Self as Tag<'_>>::Type) -> *mut <Self as Tag<'_>>::Type {
        this as *mut T::Type
    }
}

fn main() {}


