tests/incremental/source_loc_macros.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test makes sure that different expansions of the file!(), line!(),
// column!() macros get picked up by the incr. comp. hash.

// revisions:rpass1 rpass2

// compile-flags: -Z query-dep-graph

#![feature(rustc_attrs)]

#[rustc_clean(cfg="rpass2")]
fn line_same() {
    let _ = line!();
}

#[rustc_clean(cfg="rpass2")]
fn col_same() {
    let _ = column!();
}

#[rustc_clean(cfg="rpass2")]
fn file_same() {
    let _ = file!();
}

#[rustc_clean(except="hir_owner_nodes,optimized_mir", cfg="rpass2")]
fn line_different() {
    #[cfg(rpass1)]
    {
        let _ = line!();
    }
    #[cfg(rpass2)]
    {
        let _ = line!();
    }
}

#[rustc_clean(except="hir_owner_nodes,optimized_mir", cfg="rpass2")]
fn col_different() {
    #[cfg(rpass1)]
    {
        let _ = column!();
    }
    #[cfg(rpass2)]
    {
        let _ =        column!();
    }
}

fn main() {
    line_same();
    line_different();
    col_same();
    col_different();
    file_same();
}


