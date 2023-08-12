tests/ui/consts/const_let_assign2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

pub struct AA {
    pub data: [u8; 10],
}

impl AA {
    pub const fn new() -> Self {
        let mut res: AA = AA { data: [0; 10] };
        res.data[0] = 5;
        res
    }
}

static mut BB: AA = AA::new();

fn main() {
    let ptr = unsafe { &mut BB };
    for a in ptr.data.iter() {
        println!("{}", a);
    }
}


