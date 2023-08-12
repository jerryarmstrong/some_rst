tests/incremental/struct_change_nothing.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test incremental compilation tracking where we change nothing
// in between revisions (hashing should be stable).

// revisions:rpass1 rpass2
// compile-flags: -Z query-dep-graph

#![feature(rustc_attrs)]

#[cfg(rpass1)]
pub struct X {
    pub x: u32
}

#[cfg(rpass2)]
pub struct X {
    pub x: u32
}

pub struct EmbedX {
    x: X
}

pub struct Y {
    pub y: char
}

#[rustc_clean(cfg="rpass2")]
pub fn use_X() -> u32 {
    let x: X = X { x: 22 };
    x.x as u32
}

#[rustc_clean(cfg="rpass2")]
pub fn use_EmbedX(x: EmbedX) -> u32 {
    let x: X = X { x: 22 };
    x.x as u32
}

#[rustc_clean(cfg="rpass2")]
pub fn use_Y() {
    let x: Y = Y { y: 'c' };
}

pub fn main() { }


