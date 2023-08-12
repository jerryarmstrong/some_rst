src/tools/miri/tests/pass/issues/issue-5917.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct T(&'static [isize]);
static STATIC: T = T(&[5, 4, 3]);
pub fn main() {
    let T(ref v) = STATIC;
    assert_eq!(v[0], 5);
}


