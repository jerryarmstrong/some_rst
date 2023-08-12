tests/ui/consts/const_in_pattern/auxiliary/consts.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct CustomEq;

impl Eq for CustomEq {}
impl PartialEq for CustomEq {
    fn eq(&self, _: &Self) -> bool {
        false
    }
}

pub const NONE: Option<CustomEq> = None;
pub const SOME: Option<CustomEq> = Some(CustomEq);

pub trait AssocConst {
    const NONE: Option<CustomEq> = None;
    const SOME: Option<CustomEq> = Some(CustomEq);
}


