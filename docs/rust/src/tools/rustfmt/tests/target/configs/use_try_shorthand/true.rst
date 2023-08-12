src/tools/rustfmt/tests/target/configs/use_try_shorthand/true.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-use_try_shorthand: true
// Use try! shorthand

fn main() {
    let lorem = ipsum.map(|dolor| dolor.sit())?;
}


