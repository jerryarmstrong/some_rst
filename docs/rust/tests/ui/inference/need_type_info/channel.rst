tests/ui/inference/need_type_info/channel.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we suggest specifying the generic argument of `channel`
// instead of the return type of that function, which is a lot more
// complex.
use std::sync::mpsc::channel;

fn no_tuple() {
    let _data =
        channel(); //~ ERROR type annotations needed
}

fn tuple() {
    let (_sender, _receiver) =
        channel(); //~ ERROR type annotations needed
}

fn main() {
    no_tuple();
    tuple();
}


