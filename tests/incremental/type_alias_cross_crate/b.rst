tests/incremental/type_alias_cross_crate/b.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:a.rs
// revisions:rpass1 rpass2 rpass3
// compile-flags: -Z query-dep-graph

#![feature(rustc_attrs)]

extern crate a;

#[rustc_clean(except="typeck", cfg="rpass2")]
#[rustc_clean(cfg="rpass3")]
pub fn use_X() -> u32 {
    let x: a::X = 22;
    x as u32
}

#[rustc_clean(cfg="rpass2")]
#[rustc_clean(cfg="rpass3")]
pub fn use_Y() {
    let x: a::Y = 'c';
}

pub fn main() { }


