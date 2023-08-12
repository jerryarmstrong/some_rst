tests/ui/regions/regions-adjusted-lvalue-op.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check that we link regions in mutable place ops correctly - issue #41774

struct Data(i32);

trait OhNo {
    fn oh_no(&mut self, other: &Vec<Data>) { loop {} }
}

impl OhNo for Data {}
impl OhNo for [Data] {}

fn main() {
    let mut v = vec![Data(0)];
    v[0].oh_no(&v); //~ ERROR cannot borrow `v` as immutable because
    (*v).oh_no(&v); //~ ERROR cannot borrow `v` as immutable because
}


