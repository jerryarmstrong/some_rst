src/tools/rustfmt/tests/source/issue-4244.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct SS {}

pub type  A  /* A Comment */      = SS;

pub type  B // Comment
// B
= SS;

pub type C 
 /* Comment C */ = SS;

pub trait D <T> {
		type E /* Comment E */ = SS;
}

type F<'a: 'static, T: Ord + 'static>: Eq + PartialEq where T: 'static + Copy     /* x */   = Vec<u8>;


