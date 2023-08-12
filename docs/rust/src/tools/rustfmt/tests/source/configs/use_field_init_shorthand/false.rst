src/tools/rustfmt/tests/source/configs/use_field_init_shorthand/false.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-use_field_init_shorthand: false
// Use field initialization shorthand if possible.

fn main() {
    let a = Foo {
        x: x,
        y: y,
        z: z,
    };

    let b = Bar {
        x: x,
        y: y,
        #[attr]
        z: z,
        #[rustfmt::skip]
        skipped: skipped,
    };
}


