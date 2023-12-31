compiler/rustc_mir_transform/src/dump_mir.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! This pass just dumps MIR at a specified point.

use std::fs::File;
use std::io;

use crate::MirPass;
use rustc_middle::mir::write_mir_pretty;
use rustc_middle::mir::Body;
use rustc_middle::ty::TyCtxt;
use rustc_session::config::OutputType;

pub struct Marker(pub &'static str);

impl<'tcx> MirPass<'tcx> for Marker {
    fn name(&self) -> &str {
        self.0
    }

    fn run_pass(&self, _tcx: TyCtxt<'tcx>, _body: &mut Body<'tcx>) {}
}

pub fn emit_mir(tcx: TyCtxt<'_>) -> io::Result<()> {
    let path = tcx.output_filenames(()).path(OutputType::Mir);
    let mut f = io::BufWriter::new(File::create(&path)?);
    write_mir_pretty(tcx, None, &mut f)?;
    Ok(())
}


