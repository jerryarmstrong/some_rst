tests/ui/lint/lint-ctypes-73747.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#[repr(transparent)]
struct NonNullRawComPtr<T: ComInterface> {
    inner: std::ptr::NonNull<<T as ComInterface>::VTable>,
}

trait ComInterface {
    type VTable;
}

extern "C" fn invoke<T: ComInterface>(_: Option<NonNullRawComPtr<T>>) {}

fn main() {}


