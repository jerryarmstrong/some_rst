tests/rustdoc-ui/error-in-impl-trait/realistic-async.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// check-pass

mod windows {
    pub trait WinFoo {
        fn foo(&self) {}
    }

    impl WinFoo for () {}
}

#[cfg(any(windows, doc))]
use windows::*;

mod unix {
    pub trait UnixFoo {
        fn foo(&self) {}
    }

    impl UnixFoo for () {}
}

#[cfg(any(unix, doc))]
use unix::*;

async fn bar() {
    ().foo()
}


