src/tools/rust-analyzer/crates/rust-analyzer/src/cli/parse.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Read Rust code on stdin, print syntax tree on stdout.
use syntax::{AstNode, SourceFile};

use crate::cli::{flags, read_stdin};

impl flags::Parse {
    pub fn run(self) -> anyhow::Result<()> {
        let _p = profile::span("parsing");
        let text = read_stdin()?;
        let file = SourceFile::parse(&text).tree();
        if !self.no_dump {
            println!("{:#?}", file.syntax());
        }
        std::mem::forget(file);
        Ok(())
    }
}


