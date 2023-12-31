src/tools/miri/bench-cargo-miri/backtraces/src/main.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Extracted from the backtrace crate's test test_frame_conversion

use backtrace::{Backtrace, BacktraceFrame};
use std::fmt::Write;

fn main() {
    let mut frames = vec![];
    backtrace::trace(|frame| {
        let converted = BacktraceFrame::from(frame.clone());
        frames.push(converted);
        true
    });

    let mut manual = Backtrace::from(frames);
    manual.resolve();
    let frames = manual.frames();

    let mut output = String::new();
    for frame in frames {
        // Originally these were println! but we'd prefer our benchmarks to not emit a lot of
        // output to stdout/stderr. Unfortunately writeln! to a String is faster, but we still
        // manage to exercise interesting code paths in Miri.
        writeln!(output, "{:?}", frame.ip()).unwrap();
        writeln!(output, "{:?}", frame.symbol_address()).unwrap();
        writeln!(output, "{:?}", frame.module_base_address()).unwrap();
        writeln!(output, "{:?}", frame.symbols()).unwrap();
    }
    drop(output);
}


