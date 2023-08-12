tests/ui/repeat-expr/repeat-expr-in-static.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

static FOO: [isize; 4] = [32; 4];
static BAR: [isize; 4] = [32, 32, 32, 32];

pub fn main() {
    assert_eq!(FOO, BAR);
}


