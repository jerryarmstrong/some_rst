quinn-udp/src/cmsg.rs
=====================

Last edited: 2022-02-11 21:48:07

Contents:

.. code-block:: rs

    use std::{mem, ptr};

#[derive(Copy, Clone)]
#[repr(align(8))] // Conservative bound for align_of<cmsghdr>
pub struct Aligned<T>(pub T);

/// Helper to encode a series of control messages ("cmsgs") to a buffer for use in `sendmsg`.
///
/// The operation must be "finished" for the msghdr to be usable, either by calling `finish`
/// explicitly or by dropping the `Encoder`.
pub struct Encoder<'a> {
    hdr: &'a mut libc::msghdr,
    cmsg: Option<&'a mut libc::cmsghdr>,
    len: usize,
}

impl<'a> Encoder<'a> {
    /// # Safety
    /// - `hdr.msg_control` must be a suitably aligned pointer to `hdr.msg_controllen` bytes that
    ///   can be safely written
    /// - The `Encoder` must be dropped before `hdr` is passed to a system call, and must not be leaked.
    pub unsafe fn new(hdr: &'a mut libc::msghdr) -> Self {
        Self {
            cmsg: libc::CMSG_FIRSTHDR(hdr).as_mut(),
            hdr,
            len: 0,
        }
    }

    /// Append a control message to the buffer.
    ///
    /// # Panics
    /// - If insufficient buffer space remains.
    /// - If `T` has stricter alignment requirements than `cmsghdr`
    pub fn push<T: Copy + ?Sized>(&mut self, level: libc::c_int, ty: libc::c_int, value: T) {
        assert!(mem::align_of::<T>() <= mem::align_of::<libc::cmsghdr>());
        let space = unsafe { libc::CMSG_SPACE(mem::size_of_val(&value) as _) as usize };
        assert!(
            self.hdr.msg_controllen as usize >= self.len + space,
            "control message buffer too small. Required: {}, Available: {}",
            self.len + space,
            self.hdr.msg_controllen
        );
        let cmsg = self.cmsg.take().expect("no control buffer space remaining");
        cmsg.cmsg_level = level;
        cmsg.cmsg_type = ty;
        cmsg.cmsg_len = unsafe { libc::CMSG_LEN(mem::size_of_val(&value) as _) } as _;
        unsafe {
            ptr::write(libc::CMSG_DATA(cmsg) as *const T as *mut T, value);
        }
        self.len += space;
        self.cmsg = unsafe { libc::CMSG_NXTHDR(self.hdr, cmsg).as_mut() };
    }

    /// Finishes appending control messages to the buffer
    pub fn finish(self) {
        // Delegates to the `Drop` impl
    }
}

// Statically guarantees that the encoding operation is "finished" before the control buffer is read
// by `sendmsg`.
impl<'a> Drop for Encoder<'a> {
    fn drop(&mut self) {
        self.hdr.msg_controllen = self.len as _;
    }
}

/// # Safety
///
/// `cmsg` must refer to a cmsg containing a payload of type `T`
pub unsafe fn decode<T: Copy>(cmsg: &libc::cmsghdr) -> T {
    assert!(mem::align_of::<T>() <= mem::align_of::<libc::cmsghdr>());
    debug_assert_eq!(
        cmsg.cmsg_len as usize,
        libc::CMSG_LEN(mem::size_of::<T>() as _) as usize
    );
    ptr::read(libc::CMSG_DATA(cmsg) as *const T)
}

pub struct Iter<'a> {
    hdr: &'a libc::msghdr,
    cmsg: Option<&'a libc::cmsghdr>,
}

impl<'a> Iter<'a> {
    /// # Safety
    ///
    /// `hdr.msg_control` must point to memory outliving `'a` which can be soundly read for the
    /// lifetime of the constructed `Iter` and contains a buffer of cmsgs, i.e. is aligned for
    /// `cmsghdr`, is fully initialized, and has correct internal links.
    pub unsafe fn new(hdr: &'a libc::msghdr) -> Self {
        Self {
            hdr,
            cmsg: libc::CMSG_FIRSTHDR(hdr).as_ref(),
        }
    }
}

impl<'a> Iterator for Iter<'a> {
    type Item = &'a libc::cmsghdr;
    fn next(&mut self) -> Option<&'a libc::cmsghdr> {
        let current = self.cmsg.take()?;
        self.cmsg = unsafe { libc::CMSG_NXTHDR(self.hdr, current).as_ref() };
        Some(current)
    }
}


