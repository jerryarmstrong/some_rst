tests/ui/issues/issue-2063.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// test that autoderef of a type like this does not
// cause compiler to loop.  Note that no instances
// of such a type could ever be constructed.

struct T(#[allow(unused_tuple_struct_fields)] Box<T>);

trait ToStr2 {
    fn my_to_string(&self) -> String;
}

impl ToStr2 for T {
    fn my_to_string(&self) -> String { "t".to_string() }
}

#[allow(dead_code)]
fn new_t(x: T) {
    x.my_to_string();
}

fn main() {
}


