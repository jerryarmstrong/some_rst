tests/ui/coherence/conflicting-impl-with-err.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct ErrorKind;
struct Error(ErrorKind);

impl From<nope::Thing> for Error { //~ ERROR failed to resolve
    fn from(_: nope::Thing) -> Self { //~ ERROR failed to resolve
        unimplemented!()
    }
}

impl From<ErrorKind> for Error {
    fn from(_: ErrorKind) -> Self {
        unimplemented!()
    }
}

fn main() {}


