src/std/src/sys/unix/fd/tests.rs
================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use super::{FileDesc, IoSlice};
use core::mem::ManuallyDrop;

#[test]
fn limit_vector_count() {
    let stdout = ManuallyDrop::new(unsafe { FileDesc { fd: 1 } });
    let bufs = (0..1500).map(|_| IoSlice::new(&[])).collect::<Vec<_>>();
    assert!(stdout.write_vectored(&bufs).is_ok());
}


