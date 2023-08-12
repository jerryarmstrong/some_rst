tests/ui/consts/static_mut_containing_mut_ref.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

static mut STDERR_BUFFER_SPACE: [u8; 42] = [0u8; 42];

pub static mut STDERR_BUFFER: *mut [u8] = unsafe { &mut STDERR_BUFFER_SPACE };

fn main() {}


