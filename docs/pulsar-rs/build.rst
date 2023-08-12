build.rs
========

Last edited: 2022-07-13 17:30:21

Contents:

.. code-block:: rs

    extern crate prost_build;

fn main() {
    prost_build::compile_protos(&["./PulsarApi.proto"], &["./"]).unwrap();
}


