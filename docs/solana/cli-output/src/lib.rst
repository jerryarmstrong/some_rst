cli-output/src/lib.rs
=====================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #![allow(clippy::integer_arithmetic)]
mod cli_output;
pub mod cli_version;
pub mod display;
pub use cli_output::*;

pub trait QuietDisplay: std::fmt::Display {
    fn write_str(&self, w: &mut dyn std::fmt::Write) -> std::fmt::Result {
        write!(w, "{self}")
    }
}

pub trait VerboseDisplay: std::fmt::Display {
    fn write_str(&self, w: &mut dyn std::fmt::Write) -> std::fmt::Result {
        write!(w, "{self}")
    }
}


