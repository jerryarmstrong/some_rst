compiler/rustc_data_structures/src/flock/unsupported.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::io;
use std::path::Path;

#[derive(Debug)]
pub struct Lock(());

impl Lock {
    pub fn new(_p: &Path, _wait: bool, _create: bool, _exclusive: bool) -> io::Result<Lock> {
        let msg = "file locks not supported on this platform";
        Err(io::Error::new(io::ErrorKind::Other, msg))
    }

    pub fn error_unsupported(_err: &io::Error) -> bool {
        true
    }
}


