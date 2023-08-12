tests/ui/let-else/let-else-slicing-error.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue #92069


fn main() {
    let nums = vec![5, 4, 3, 2, 1];
    let [x, y] = nums else { //~ ERROR expected an array or slice
        return;
    };
}


