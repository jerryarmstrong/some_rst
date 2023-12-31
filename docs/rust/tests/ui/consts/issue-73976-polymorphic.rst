tests/ui/consts/issue-73976-polymorphic.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test is from #73976. We previously did not check if a type is monomorphized
// before calculating its type id, which leads to the bizarre behaviour below that
// TypeId of a generic type does not match itself.
//
// This test case should either run-pass or be rejected at compile time.
// Currently we just disallow this usage and require pattern is monomorphic.

#![feature(const_type_id)]
#![feature(const_type_name)]

use std::any::{self, TypeId};

pub struct GetTypeId<T>(T);

impl<T: 'static> GetTypeId<T> {
    pub const VALUE: TypeId = TypeId::of::<T>();
}

const fn check_type_id<T: 'static>() -> bool {
    matches!(GetTypeId::<T>::VALUE, GetTypeId::<T>::VALUE)
    //~^ ERROR constant pattern depends on a generic parameter
    //~| ERROR constant pattern depends on a generic parameter
}

pub struct GetTypeNameLen<T>(T);

impl<T: 'static> GetTypeNameLen<T> {
    pub const VALUE: usize = any::type_name::<T>().len();
}

const fn check_type_name_len<T: 'static>() -> bool {
    matches!(GetTypeNameLen::<T>::VALUE, GetTypeNameLen::<T>::VALUE)
    //~^ ERROR constant pattern depends on a generic parameter
    //~| ERROR constant pattern depends on a generic parameter
}

fn main() {
    assert!(check_type_id::<usize>());
    assert!(check_type_name_len::<usize>());
}


