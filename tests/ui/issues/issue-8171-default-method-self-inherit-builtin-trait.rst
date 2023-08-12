tests/ui/issues/issue-8171-default-method-self-inherit-builtin-trait.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

/*

#8171 Self is not recognised as implementing kinds in default method implementations

*/

fn require_send<T: Send>(_: T){}

trait TragicallySelfIsNotSend: Send + Sized {
    fn x(self) {
        require_send(self);
    }
}

pub fn main(){}


