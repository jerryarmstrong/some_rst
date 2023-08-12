src/tools/clippy/tests/ui/multi_assignments.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::multi_assignments)]
fn main() {
    let (mut a, mut b, mut c, mut d) = ((), (), (), ());
    a = b = c;
    a = b = c = d;
    a = b = { c };
    a = { b = c };
    a = (b = c);
}


