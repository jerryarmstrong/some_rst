tests/ui/issues/issue-3847.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
mod buildings {
    pub struct Tower { pub height: usize }
}

pub fn main() {
    let sears = buildings::Tower { height: 1451 };
    let h: usize = match sears {
        buildings::Tower { height: h } => { h }
    };

    println!("{}", h);
}


