tests/ui/coherence/auxiliary/coherence_copy_like_lib.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]
#![feature(fundamental)]

pub trait MyCopy { }
impl MyCopy for i32 { }

pub struct MyStruct<T>(T);

#[fundamental]
pub struct MyFundamentalStruct<T>(T);


