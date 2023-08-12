tests/ui/lint/lint-ctypes-73251-2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
#![deny(improper_ctypes)]

pub trait TraitA {
    type Assoc;
}

impl TraitA for u32 {
    type Assoc = u32;
}

pub trait TraitB {
    type Assoc;
}

impl<T> TraitB for T
where
    T: TraitA,
{
    type Assoc = <T as TraitA>::Assoc;
}

type AliasA = impl TraitA<Assoc = u32>;

type AliasB = impl TraitB<Assoc = AliasA>;

fn use_of_a() -> AliasA {
    3
}

fn use_of_b() -> AliasB {
    3
}

extern "C" {
    pub fn lint_me() -> <AliasB as TraitB>::Assoc; //~ ERROR: uses type `AliasA`
}

fn main() {}


