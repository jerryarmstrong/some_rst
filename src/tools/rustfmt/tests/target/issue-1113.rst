src/tools/rustfmt/tests/target/issue-1113.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn foo() -> fmt::Result
//pub fn writeStringToken
{
    panic!()
}

pub fn foo() -> fmt::Result // pub fn writeStringToken
{
    panic!()
}

pub fn foo() -> fmt::Result /* pub fn writeStringToken */ {
    panic!()
}

pub fn foo() -> fmt::Result
/* pub fn writeStringToken */ {
    panic!()
}

pub fn foo() -> fmt::Result
/* pub fn writeStringToken */
{
    panic!()
}

pub fn foo() -> fmt::Result /*
                             *
                             *
                             */
{
    panic!()
}


