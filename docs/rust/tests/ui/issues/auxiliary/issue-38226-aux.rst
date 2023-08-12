tests/ui/issues/auxiliary/issue-38226-aux.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="rlib"]

#[inline(never)]
pub fn foo<T>() {
    let _: Box<SomeTrait> = Box::new(SomeTraitImpl);
}

pub fn bar() {
    SomeTraitImpl.bar();
}

mod submod {
    pub trait SomeTrait {
        fn bar(&self) {
            panic!("NO")
        }
    }
}

use self::submod::SomeTrait;

pub struct SomeTraitImpl;
impl SomeTrait for SomeTraitImpl {}


