compiler/rustc_save_analysis/src/errors.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use rustc_macros::Diagnostic;

use std::path::Path;

#[derive(Diagnostic)]
#[diag(save_analysis_could_not_open)]
pub(crate) struct CouldNotOpen<'a> {
    pub file_name: &'a Path,
    pub err: std::io::Error,
}


