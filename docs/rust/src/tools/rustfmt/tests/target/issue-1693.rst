src/tools/rustfmt/tests/target/issue-1693.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn issue1693() {
    let pixel_data = vec![
        (
            f16::from_f32(0.82),
            f16::from_f32(1.78),
            f16::from_f32(0.21)
        );
        256 * 256
    ];
}


