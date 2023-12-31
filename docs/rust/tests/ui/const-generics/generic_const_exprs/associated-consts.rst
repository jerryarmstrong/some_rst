tests/ui/const-generics/generic_const_exprs/associated-consts.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

pub trait BlockCipher {
    const BLOCK_SIZE: usize;
}

struct FooCipher;
impl BlockCipher for FooCipher {
    const BLOCK_SIZE: usize = 64;
}

struct BarCipher;
impl BlockCipher for BarCipher {
    const BLOCK_SIZE: usize = 32;
}

pub struct Block<C>(#[allow(unused_tuple_struct_fields)] C);

pub fn test<C: BlockCipher, const M: usize>()
where
    [u8; M - C::BLOCK_SIZE]: Sized,
{
    let _ = [0; M - C::BLOCK_SIZE];
}

fn main() {
    test::<FooCipher, 128>();
    test::<BarCipher, 64>();
}


