tests/run-make-fulldeps/foreign-rust-exceptions/foo.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(c_unwind)]

#[cfg_attr(not(windows), link(name = "bar"))]
#[cfg_attr(windows, link(name = "bar.dll"))]
extern "C-unwind" {
    fn panic();
}

fn main() {
    let _ = std::panic::catch_unwind(|| {
        unsafe { panic() };
    });
}


