tests/ui/resolve/issue-6702.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Monster {
    damage: isize
}


fn main() {
    let _m = Monster();
    //~^ ERROR expected function, tuple struct or tuple variant, found struct `Monster`
}


