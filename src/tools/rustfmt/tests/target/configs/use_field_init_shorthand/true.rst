src/tools/rustfmt/tests/target/configs/use_field_init_shorthand/true.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-use_field_init_shorthand: true
// Use field initialization shorthand if possible.

fn main() {
    let a = Foo { x, y, z };

    let b = Bar {
        x,
        y,
        #[attr]
        z,
        #[rustfmt::skip]
        skipped: skipped,
    };
}


