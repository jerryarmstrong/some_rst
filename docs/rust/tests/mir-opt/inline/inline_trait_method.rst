tests/mir-opt/inline/inline_trait_method.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z span_free_formats

fn main() {
    println!("{}", test(&()));
}

// EMIT_MIR inline_trait_method.test.Inline.after.mir
fn test(x: &dyn X) -> u32 {
    x.y()
}

trait X {
    fn y(&self) -> u32 {
        1
    }
}

impl X for () {
    fn y(&self) -> u32 {
        2
    }
}


