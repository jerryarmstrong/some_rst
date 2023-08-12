src/tools/clippy/tests/ui/seek_from_current.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![warn(clippy::seek_from_current)]

use std::fs::File;
use std::io::{self, Seek, SeekFrom, Write};

#[clippy::msrv = "1.50"]
fn _msrv_1_50() -> io::Result<()> {
    let mut f = File::create("foo.txt")?;
    f.write_all(b"Hi!")?;
    f.seek(SeekFrom::Current(0))?;
    f.seek(SeekFrom::Current(1))?;
    Ok(())
}

#[clippy::msrv = "1.51"]
fn _msrv_1_51() -> io::Result<()> {
    let mut f = File::create("foo.txt")?;
    f.write_all(b"Hi!")?;
    f.seek(SeekFrom::Current(0))?;
    f.seek(SeekFrom::Current(1))?;
    Ok(())
}

fn main() {}


