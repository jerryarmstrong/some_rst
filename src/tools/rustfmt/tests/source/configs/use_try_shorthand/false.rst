src/tools/rustfmt/tests/source/configs/use_try_shorthand/false.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-use_try_shorthand: false
// Use try! shorthand

fn main() {
    let lorem = try!(ipsum.map(|dolor| dolor.sit()));
}


