tests/ui/mir/mir_struct_with_assoc_ty.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::marker::PhantomData;

pub trait DataBind {
    type Data;
}

impl<T> DataBind for Global<T> {
    type Data = T;
}

pub struct Global<T>(PhantomData<T>);

pub struct Data {
    pub offsets: <Global<[u32; 2]> as DataBind>::Data,
}

fn create_data() -> Data {
    let mut d = Data { offsets: [1, 2] };
    d.offsets[0] = 3;
    d
}


fn main() {
    let d = create_data();
    assert_eq!(d.offsets[0], 3);
    assert_eq!(d.offsets[1], 2);
}


