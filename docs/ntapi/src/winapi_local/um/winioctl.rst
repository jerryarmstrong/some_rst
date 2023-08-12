src/winapi_local/um/winioctl.rs
===============================

Last edited: 2023-04-20 23:00:37

Contents:

.. code-block:: rs

    #[inline]
pub(crate) const fn CTL_CODE(DeviceType: u32, Function: u32, Method: u32, Access: u32) -> u32 {
    (DeviceType << 16) | (Access << 14) | (Function << 2) | Method
}


