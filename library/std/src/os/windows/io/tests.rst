library/std/src/os/windows/io/tests.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[test]
fn test_niche_optimizations_socket() {
    use crate::mem::size_of;
    use crate::os::windows::io::{
        BorrowedSocket, FromRawSocket, IntoRawSocket, OwnedSocket, RawSocket,
    };

    assert_eq!(size_of::<Option<OwnedSocket>>(), size_of::<RawSocket>());
    assert_eq!(size_of::<Option<BorrowedSocket<'static>>>(), size_of::<RawSocket>(),);
    unsafe {
        #[cfg(target_pointer_width = "32")]
        let (min, max) = (i32::MIN as u32, i32::MAX as u32);
        #[cfg(target_pointer_width = "64")]
        let (min, max) = (i64::MIN as u64, i64::MAX as u64);

        assert_eq!(OwnedSocket::from_raw_socket(min).into_raw_socket(), min);
        assert_eq!(OwnedSocket::from_raw_socket(max).into_raw_socket(), max);
        assert_eq!(Some(OwnedSocket::from_raw_socket(min)).unwrap().into_raw_socket(), min);
        assert_eq!(Some(OwnedSocket::from_raw_socket(max)).unwrap().into_raw_socket(), max);
    }
}


