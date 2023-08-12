tests/ui/type-alias-impl-trait/multiple_definitions.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

use std::marker::PhantomData;

pub struct ConcreteError {}
pub trait IoBase {}
struct X {}
impl IoBase for X {}

pub struct ClusterIterator<B, E, S = B> {
    pub fat: B,
    phantom_s: PhantomData<S>,
    phantom_e: PhantomData<E>,
}

pub struct FileSystem<IO: IoBase> {
    pub disk: IO,
}

impl<IO: IoBase> FileSystem<IO> {
    pub fn cluster_iter(&self) -> ClusterIterator<impl IoBase + '_, ConcreteError> {
        ClusterIterator {
            fat: X {},
            phantom_s: PhantomData::default(),
            phantom_e: PhantomData::default(),
        }
    }
}

fn main() {}


