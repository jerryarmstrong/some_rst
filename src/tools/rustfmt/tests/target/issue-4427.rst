src/tools/rustfmt/tests/target/issue-4427.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const A: usize =
    // Some constant
    2;

const B: usize =
    /* constant */
    3;

const C: usize = /* foo */ 5;

const D: usize = // baz
    /*    Some constant */
    /* ba */
    {
        3
        // foo
    };
const E: usize = /* foo */ 5;
const F: usize = { 7 };
const G: usize =
    /* foooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000xx00 */
    5;
const H: usize = /* asdfasdf */
    match G > 1 {
        true => 1,
        false => 3,
    };

pub static FOO_BAR: Vec<u8> = //f
    { vec![] };


