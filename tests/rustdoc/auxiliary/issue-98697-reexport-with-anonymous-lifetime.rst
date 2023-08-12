tests/rustdoc/auxiliary/issue-98697-reexport-with-anonymous-lifetime.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// When reexporting this function, make sure the anonymous lifetimes are not rendered.
///
/// https://github.com/rust-lang/rust/issues/98697
pub fn repro<F>()
where
    F: Fn(&str),
{
    unimplemented!()
}

pub struct Extra;

pub trait MyTrait<T> {
    fn run() {}
}

impl MyTrait<&Extra> for Extra {}


