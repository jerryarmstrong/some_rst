tests/ui/binop/issue-3820.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Thing {
    x: isize
}

impl Thing {
    fn mul(&self, c: &isize) -> Thing {
        Thing {x: self.x * *c}
    }
}

fn main() {
    let u = Thing {x: 2};
    let _v = u.mul(&3); // This is ok
    let w = u * 3; //~ ERROR cannot multiply `Thing` by `{integer}`
}


